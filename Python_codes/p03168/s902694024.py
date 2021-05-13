import numpy as np

n = int(input())

dp = np.zeros(n + 1)
dp[0] = 1.

for p in map(float, input().split()):
  tmp = (1. - p) * dp
  tmp[1:] += p * dp[:-1]
  dp = tmp

print(dp[n // 2 + 1:].sum())