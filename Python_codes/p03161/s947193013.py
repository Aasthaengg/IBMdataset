import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())

import numpy as np

H = np.array(list(map(int,readline().split())),dtype = int)

dp = np.zeros(N, dtype = int)

for i in range(1, N):
  dp[i] = (dp[max(0,i - K):i] + abs(H[max(0,i - K):i] - H[i])).min()

print(dp[-1])