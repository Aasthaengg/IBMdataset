N,K = map(int,input().split())
import numpy as np
H = np.array(input().split(), dtype = int)

INF = 10 ** 9 + 1
dp = np.full(N,INF,dtype = int)
dp[0] = 0

for i in range(1, N):
  dp[i] = min(dp[max(i - K,0):i] + np.abs(H[max(i - K,0):i] - H[i]))

print(dp[-1])