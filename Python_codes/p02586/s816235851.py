import numpy as np
from numba import njit, i8


@njit(i8(i8, i8, i8[:, :]), cache=True)
def solve(R, C, items):
    dp = np.zeros((R + 1, C + 1, 4), dtype=np.int64)
    for i in range(R):
        for j in range(C):
            for k in range(2, -1, -1):
                dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + items[i][j])
            for k in range(4):
                dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][k])
                dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
    return dp[R][C - 1][0]


R, C, K, *rcv = map(int, open(0).read().split())
items = np.zeros((R + 1, C + 1), dtype=np.int64)
for r, c, v in zip(*[iter(rcv)] * 3):
    items[r - 1][c - 1] = v
print(solve(R, C, items))
