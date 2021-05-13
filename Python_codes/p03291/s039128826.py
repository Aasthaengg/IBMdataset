import numpy as np


dp = np.zeros((2, 4), dtype=np.int64)
mod = int(1e9+7)
dp[0][0] = 1
for s in input():
    if s == '?':
        dp[1] = dp[0]*3
        dp[1][1:] += dp[0][:3]
    else:
        dp[1] = dp[0]
        if s == 'A':
            dp[1][1] += dp[0][0]
        elif s == 'B':
            dp[1][2] += dp[0][1]
        elif s == 'C':
            dp[1][3] += dp[0][2]
    dp[0] = np.remainder(dp[1], mod)
print(dp[0][3])