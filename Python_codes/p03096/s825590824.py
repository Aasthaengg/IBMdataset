N = int(input())
C = [int(input()) for _ in range(N)]
mod = int(1e9+7)

from itertools import groupby
x = [0] + [k for k, g in groupby(C)]

dp = [0]*(len(x)) # i個目までで何通りあるか
dp[0] = 1
memo = {}

for i in range(1, len(x)):
    c = x[i]
    memo[c] = (memo.get(c,0) + dp[i-1])%mod
    dp[i] = memo[c]

print(dp[-1])