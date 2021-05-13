# solution
import io
from scipy.misc import comb

nim, mike, kite = map(int, input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)
print(sum(V[:mike]) / mike)
Ath_CNT = V.count(V[mike - 1])
V_than_Ath_CNT = len([v for v in V if v > V[mike - 1]])
if max(V) == V[mike - 1]:
    ans = 0
    for k in range(mike, kite + 1):
        ans += comb(Ath_CNT, k, 1)
else:
    ans = comb(Ath_CNT, mike - V_than_Ath_CNT, 1)
print(ans)
