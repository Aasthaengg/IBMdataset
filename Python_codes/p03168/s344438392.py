import numpy as np
N = int(input())
dp = np.zeros(N+1, dtype=np.float64)
p_lst = list(map(float, input().split()))
dp[0] = 1
for p in p_lst:
  next_dp = dp * (1-p)
  next_dp[1:] += dp[:-1] * p
  dp = next_dp

print(dp[N//2+1:].sum())