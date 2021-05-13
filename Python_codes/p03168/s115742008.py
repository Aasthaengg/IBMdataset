import numpy as np

n = int(input())
P = list(map(float, input().split()))
dp = np.zeros((n+1, n+1))
dp[0, 0] = 1
for i in range(n):
  dp[i+1, 0] = dp[i, 0] * (1-P[i])
  dp[i+1, 1:] = dp[i, :-1]*P[i] + dp[i, 1:]*(1-P[i])
print(dp[n, 1+n//2:].sum())