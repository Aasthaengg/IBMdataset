#!/usr/bin/env python

s = int(input())
mod = 10**9+7

if s == 1 or s == 2:
    print(0)
    exit()

dp = [0 for _ in range(s+1)]
dp[0] = dp[1] = dp[2] = 0 

for i in range(s+1):
    for j in range(i-3, 2, -1):
        dp[i] += dp[j]
    dp[i] += 1

ans = dp[s]%mod
print(ans)

