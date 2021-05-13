import numpy as np
import sys
buf = sys.stdin.buffer

N = int(input())
M = N // 2 + 1
P = np.array(input().split(),dtype = float)

dp = np.zeros([(N + 1),(N + 1)])
dp[0][0] = 1.0

for i in range(N):
  tmp = dp[i].copy()
  dp[i + 1] = tmp * (1 - P[i])
  tmp = np.roll(tmp,1)
  dp[i + 1] += tmp * P[i] 
  
print(sum(dp[-1][M:]))
