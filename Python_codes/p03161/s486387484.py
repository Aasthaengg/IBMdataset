import numpy as np
N, K = map(int, input().split())
h = np.array(list(map(int, input().split())) + [0]*K, dtype=np.int64)
H = np.array(h)
dp = np.full(N + K, 10 ** 10, dtype=np.int64)
dp[0] = 0
for i in range(1, N):
    dp[i:i + K] = np.minimum(dp[i:i + K],
                             np.abs(H[i:i + K] - H[i - 1]) + dp[i - 1])
print(dp[N - 1]) 