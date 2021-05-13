import numpy as np
n, k = map(int,input().split())
H = np.array(input().split(), dtype=np.int64)

INF = 10 ** 9 + 1
dp = np.full(n, INF, dtype=np.int64)
dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[max(i - k,0):i] + np.abs(H[max(i - k,0):i] - H[i]))

print(dp[-1])