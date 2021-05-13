import numpy as np
N = int(input())
P = np.array(input().split(), dtype=float)

dp = np.zeros(N + 1, dtype=float)
dp[0] = 1 - P[0]
dp[1] = P[0]

for i in range(N - 1):
    newDP = dp * (1 - P[i + 1])
    newDP[1:] += dp[:-1] * P[i + 1]
    dp = newDP.copy()

n = (N + 1) // 2
ans = dp[n:].sum()
print(ans)
