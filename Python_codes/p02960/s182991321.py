import numpy as np
from numba import njit, i8

S = input()
MOD = 10 ** 9 + 7

dp = np.zeros(13, dtype=int)
dp[0] = 1


@njit(cache=True)
def q_mark(dp):
    new_dp = np.zeros(13, dtype=i8)
    for i in range(13):
        new_dp[np.arange(i, i + 10) % 13] += dp[i]
        new_dp %= MOD
    return new_dp


for s in S:
    # 4 == pow(10, -1, 13)
    dp = dp[np.arange(0, 52, 4) % 13]
    if s == '?':
        dp = q_mark(dp)
    else:
        dp = np.roll(dp, int(s))
print(dp[5])
