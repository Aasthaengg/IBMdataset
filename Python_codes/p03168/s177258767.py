import numpy as np

N = int(input())
P = list(map(float, input().split()))

dp = np.zeros(N + 2)
dp[1] = 1

for p in P:
    q = 1 - p
    dp[1:] = dp[:N + 1] * p + dp[1:] * q

# print (dp)
print (sum(dp[N // 2 + 2:]))