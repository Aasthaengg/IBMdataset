import sys
input = sys.stdin.readline

N, D, a = [int(x) for x in input().split()]
XH = []
for _ in range(N):
    XH.append([int(x) for x in input().split()])
XH.sort()

#####segfunc######
def segfunc(x,y):
    return x + y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])

def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#入力
n = N
A = [0] * N

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

#init
init(A)

import bisect

X = []
H = []
for i in XH:
    X.append(i[0])
    H.append(i[1])
ans = 0
for i in range(N):
    x, h = X[i], H[i]
    idx_left = bisect.bisect_left(X, x - 2 * D)
    idx_right = i
    tmp = query(idx_left, idx_right)
    if tmp < h:
        h -= tmp
        cnt = h // a + int(h % a != 0)
        ans += cnt
        update(i, a * cnt)
print(ans)
        
