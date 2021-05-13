import numpy as np


dp = np.zeros((2, 4), dtype=np.int64)
mod = 1e9+7
dp[0][0] = 1
for s in input():
    if s == '?':
        dp[1] = dp[0]*3
        dp[1][1:] += dp[0][:3]
        dp[1] = np.remainder(dp[1], mod)
    else:
        dp[1] = dp[0]
        if s == 'A':
            dp[1][1] += dp[0][0]
            dp[1][1] = np.remainder(dp[1][1], mod)
        elif s == 'B':
            dp[1][2] += dp[0][1]
            dp[1][2] = np.remainder(dp[1][2], mod)
        elif s == 'C':
            dp[1][3] += dp[0][2]
            dp[1][3] = np.remainder(dp[1][3], mod)
    dp[0] = dp[1]
print(dp[0][3])
