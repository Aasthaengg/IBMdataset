import math
import sys

N,K = list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))

dp = [False] * (K + 1)
for i in range(K + 1):
    for a in As:
        if i + a <= K:
            dp[i + a] |= (not dp[i])
ans = "First" if dp[K] else "Second"
print(ans)

