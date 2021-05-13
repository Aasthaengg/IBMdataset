import numpy as np
N = int(input())
P = tuple(map(float, input().split()))

dp = np.zeros(N + 1, dtype=float)
dp[0] = 1

for p in P:
    newDP = dp * (1-p)
    newDP[1:] += dp[:-1] * p
    dp = newDP

n = (N + 1) // 2
ans = dp[n:].sum()
print(ans)
