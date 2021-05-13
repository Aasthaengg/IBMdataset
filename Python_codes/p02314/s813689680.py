# -*- coding: utf-8 -*-
n, m = map(int,input().split())
c = [int(i) for i in input().split()] 

dp = [100000 for _ in range(n+1)]
dp[0] = 0
for i in range(1, n+1):
    for j in c:
        if 0 <= i - j:
            dp[i] = min(dp[i - j] + 1, dp[i])
print(dp[n])

