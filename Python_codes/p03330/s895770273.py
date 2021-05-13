from itertools import permutations

import numpy as np
from numba import njit, i8


@njit(i8[:, :](i8, i8, i8[:, :], i8[:, :]), cache=True)
def calc_cost(N, C, D, c):
    cost = np.zeros((C, 3), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            for k in range(C):
                cost[k][(i + j) % 3] += D[c[i][j] - 1][k]
    return cost


N, C, *Dc = map(int, open(0).read().split())
D = np.array(Dc[: C * C], dtype=np.int64).reshape(C, C)
c = np.array(Dc[C * C :], dtype=np.int64).reshape(N, N)
cost = calc_cost(N, C, D, c)

ans = min(
    sum(cost[c][i] for i, c in enumerate(colors))
    for colors in permutations(range(C), 3)
)
print(ans)
