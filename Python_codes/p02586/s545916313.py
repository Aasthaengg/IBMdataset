import numpy as np
from numba import njit


@njit
def solve():
    dp = np.zeros((R + 1, C + 1, 4), dtype=np.int64)
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            for k in range(4):
                dp[i][j][k] = max(dp[i][j - 1][k], dp[i - 1][j][3])
            if items[i][j] == 0:
                continue
            for k in range(3, 0, -1):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j][k - 1] + items[i][j])
    return dp[R][C][-1]


R, C, K, *rcv = map(int, open(0).read().split())

items = np.zeros((R + 1, C + 1), dtype=np.int32)
for r, c, v in zip(*[iter(rcv)] * 3):
    items[r][c] = v

print(solve())
