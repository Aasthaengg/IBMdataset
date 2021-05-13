from numba import njit, i8
import numpy as np


@njit(i8[:](i8))
def solve(N):
    # 4 * h * n * w == N * (h * n + n * w + w * h)
    for i in range(3501):
        for j in range(3501):
            num = N * i * j
            den = 4 * i * j - N * (i + j)
            if den <= 0:
                continue
            if num % den == 0:
                return np.array((i, j, num // den), dtype=np.int64)
    return np.zeros(3, dtype=np.int64)


print(*solve(int(input())))
