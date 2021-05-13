from bisect import bisect_left
import random
import time
import math


#入力
D = int(input())
C = [int(c) for c in input().split()]
S = []
for _ in range(D):
    s = [int(x) for x in input().split()]
    S.append(s)
#初期解
T = []
for _ in range(D):
    t = random.randrange(26)
    T.append(t)


last_day = [[-1] for _ in range(26)]
for d in range(D):
    test = T[d]
    last_day[test].append(d)
for i in range(26):
    last_day[i].append(D)


T0 = 10000
time_start = time.perf_counter()
while True:
    time_now = time.perf_counter()
    if time_now - time_start > 1.80:
        break
    #時間を正規化して温度を設定
    time_n = (time_now - time_start) / 1.80
    T1 = T0 ** (1 - time_n)
    for _ in range(100):
        #ランダムな日のテストをランダムに入れ替え
        d = random.randrange(365)
        q = random.randrange(26)
        old = T[d]
        T[d] = q
        #日程dでの元のテストold
        l = last_day[old]
        ind_old = l.index(d)
        dd_left = l[ind_old] - l[ind_old-1] - 1
        dd_right = l[ind_old+1] - l[ind_old] - 1
        dd = l[ind_old+1] - l[ind_old-1] - 1
        dif_old = C[old] * (((dd_left * (dd_left + 1)) // 2) + ((dd_right * (dd_right + 1)) // 2) - ((dd * (dd + 1)) // 2))
        #日程dでのテストq
        l = last_day[q]
        ind_q = bisect_left(last_day[q],d)
        dd_left = d - l[ind_q-1] - 1
        dd_right = l[ind_q] - d - 1
        dd = l[ind_q] - l[ind_q-1] - 1
        dif_q = C[q] * (((dd * (dd + 1)) // 2) - ((dd_left * (dd_left + 1)) // 2) - ((dd_right * (dd_right + 1)) // 2))
        #変更による差
        dif_s = dif_old + dif_q - S[d][old] + S[d][q]
        if (dif_s > 0) or (math.exp(dif_s / T1) > random.random()):
            del last_day[old][ind_old]
            last_day[q].insert(ind_q,d)
        else:
            T[d] = old
for d in range(365):
    print(T[d] + 1)

