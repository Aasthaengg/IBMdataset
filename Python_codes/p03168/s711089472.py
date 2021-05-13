N = int(input())
p = list(map(float, input().split()))

import numpy as np
dp = np.zeros(N+1)
dp[0] = 1

for i in range(N):
    dp[1:] = dp[1:]*(1-p[i]) + dp[:-1]*p[i]
    dp[0] *= (1-p[i])

print(sum(dp[int(N/2)+1:] ))