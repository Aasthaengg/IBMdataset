import numpy as np

N = int(input())
P = list(map(float, input().split()))

dp = np.zeros(N+1)
dp[0] = 1

for i in range(1, N+1):
  dp[1:] = dp[:-1]*P[i-1] + dp[1:]*(1-P[i-1])

print(dp[(N+1)//2])

