# 貪欲法 + 山登り法 + 3点スワップ操作 + アニーリング
import time
s__ = time.time()
limit = 1.9
#limit = 10

from numba import njit
import numpy as np

d = int(input())
cs = list(map(int, input().split()))
cs = np.array(cs, dtype=np.int64)
sm = [list(map(int, input().split())) for _ in range(d)]
sm = np.array(sm, dtype=np.int64)

@njit('i8(i8[:], i8)', cache=True)
def total_satisfaction(ts, d):
    ls = np.zeros(26, dtype=np.int64)
    s = 0
    for i in range(d):
        t = ts[i]
        t -= 1
        s += sm[i][t]
        ls[t] = i + 1

        dv = cs * ((i+1) - ls)
        s -= dv.sum()
    return s

@njit('i8(i8, i8[:], f8)', cache=True)
def loop(mxsc, ts, tmpr):
    it = 50
    rds = np.random.randint(0, 5, (it,))
    rdd = np.random.randint(1, d, (it,))
    rdq = np.random.randint(1, 26, (it,))
    rdx = np.random.randint(1, 12, (it,))
    rdy = np.random.randint(1, 6, (it,))
    c1 = 1
    c2 = 4
    for i in range(it):
        bk1 = 0
        bk2 = 0
        bk3 = 0
        if rds[0] <= c1:
            # trailing
            di = rdd[i]
            qi = rdq[i]

            bk1 = ts[di]
            ts[di] = qi
        elif rds[0] <= c2:
            # swap
            di = rdd[i]
            xi = rdx[i]
            if di + xi >= d:
                xi = di - xi
            else:
                xi = di + xi
            
            bk1 = ts[di]
            bk2 = ts[xi]
            ts[di] = bk2
            ts[xi] = bk1
        else:
            # triswap
            di = rdd[i]
            xi = rdx[i]
            if di + xi >= d:
                xi = di - xi
            else:
                xi = di + xi
            yi = rdy[i]
            if xi + yi >= d:
                yi = xi - yi
            else:
                yi = xi + yi
            
            bk1 = ts[di]
            bk2 = ts[xi]
            bk3 = ts[yi]
            ts[di] = bk2
            ts[xi] = bk3
            ts[yi] = bk1

        sc = total_satisfaction(ts, d)

        delta = sc - mxsc
        if delta > 0:
            #print('d>0', mxsc, '->', sc)
            #print(mxsc, '->', sc)
            mxsc = sc
        else:
            # Random < e^(Δ/T) の場合も更新
            exp = np.exp(delta / tmpr)
            #if i == 0:print('delta=', delta, 'tmpr=', tmpr, exp)
            r = np.random.random()
            if r <= exp:
                #print('d<0', mxsc, '->', sc, delta, tmpr, exp)
                mxsc = sc
            else:
                # 最大値を更新しなかったら戻す
                if rds[0] <= c1:
                    ts[di] = bk1
                elif rds[0] <= c2:
                    ts[di] = bk1
                    ts[xi] = bk2
                else:
                    ts[di] = bk1
                    ts[xi] = bk2
                    ts[yi] = bk3

    return mxsc

@njit('i8[:]()', cache=True)
def greedy():
    ts = np.array([0] * d, dtype=np.int64)
    for i in range(d):
        mx = -1e10
        mxt = None
        for t in range(1, 26+1):
            ts[i] = t
            s = total_satisfaction(ts, i + 1)
            if s > mx:
                mx = s
                mxt = t
        ts[i] = mxt
    return ts

ts = greedy()
#ts = np.random.randint(1, 26, (d,)).astype(np.int64)
mxsc = total_satisfaction(ts, d)
mxbk = mxsc

# annealing vars
t0 = 2e3
t1 = 6e2

s_ = time.time()
mxsc = loop(mxsc, ts, t0)
e_ = time.time()

consume = s_ - s__
elapsed = e_ - s_
#print('consume:', consume)
#print('elapsed:', elapsed)

if consume < limit:
    lp = int((limit - consume) / elapsed)
    for i in range(lp):
        t = i / lp
        tmpr = np.power(t0, 1 - t) * np.power(t1, t)
        mxsc = loop(mxsc, ts, tmpr)
        #print(mxsc)

for t in ts:    print(t)
#print(mxbk, mxsc)
#print(time.time() - s__)
#print(mxsc)
