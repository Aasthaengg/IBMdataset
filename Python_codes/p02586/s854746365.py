import numpy as np
from numba import njit, i8


@njit(i8[:](i8[:]), cache=True)
def max_acc(li):
    res = li.copy()
    cur_max = res[0]
    for i in range(len(li)):
        if res[i] > cur_max:
            cur_max = res[i]
        res[i] = cur_max
    return res


@njit(i8(i8, i8, i8[:, :]), cache=True)
def solve(R, C, goods):
    dp = np.zeros(C + 1, dtype=np.int64)
    for i in range(R):
        dp[1:] += goods[i]
        dp = max_acc(dp)
        for _ in range(2):
            dp[1:] = np.maximum(dp[:-1] + goods[i], dp[1:])
            dp = max_acc(dp)
    return dp[-1]


R, C, K, *rcv = map(int, open(0).read().split())
goods = np.zeros((R, C), dtype=np.int64)
for r, c, v in zip(*[iter(rcv)] * 3):
    goods[r - 1][c - 1] = v
print(solve(R, C, goods))
