# 問題C
import numpy as np
import warnings
warnings.filterwarnings('ignore')

N = int(input())
h = np.array([list(map(int, input().split())) for _ in range(N)])

h = h.reshape(N, 3)

dp = np.array([[0] * h.shape[1]] * h.shape[0])
dp[0, :] = h[0, :]
for i in range(1, N):
    dp[i, 0] = max(dp[i-1, 1], dp[i-1, 2])+h[i, 0]
    dp[i, 1] = max(dp[i-1, 0], dp[i-1, 2])+h[i, 1]
    dp[i, 2] = max(dp[i-1, 0], dp[i-1, 1])+h[i, 2]

print(max(dp[-1, ]))
