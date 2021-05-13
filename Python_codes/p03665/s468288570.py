#!/usr/bin/env python3
n, p, *a = map(int, open(0).read().split())
dp = [0] * (n + 1)
dp[0] = 1 if p == 0 else 0
for i in range(1, n + 1):
    if a[i - 1] % 2:
        dp[i] = 2**(i - 1)
    else:
        dp[i] = 2 * dp[i - 1]
print(dp[n])
