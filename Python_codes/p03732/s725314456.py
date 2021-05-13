from collections import defaultdict
from copy import copy
N,W = map(int,input().split())
src = [tuple(map(int,input().split())) for i in range(N)]

dp = defaultdict(lambda: 0)
dp[0] = 0
for w,v in src:
    dp2 = copy(dp)
    for pw,pv in dp.items():
        if pw+w > W: continue
        defv = dp[pw+w] if pw+w in dp else 0
        dp2[pw+w] = max(defv, pv+v)
    dp = dp2
print(max(dp.values()))