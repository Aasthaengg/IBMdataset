import numpy as np
from numba import njit

n, k = map(int, input().split())
arr = np.array(list(map(int, input().split())))


@njit
def solve(n, k, arr):
    for i in range(min(k, 50)):
        tmp_arr = np.zeros(n + 2, np.int64)
        for i, power in enumerate(arr):
            tmp_arr[max(0, i - power + 1)] += 1
            tmp_arr[min(n + 1, i + power + 2)] -= 1
        arr = np.cumsum(tmp_arr)[1:-1]
    return arr


print(*solve(n, k, arr))