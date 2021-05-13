import numba
from numba import njit, i8
import sys
import numpy as np
read = sys.stdin.readline


@njit((i8, i8[:], i8[:]), cache=True)
def main(n, a, b):
    ans = 0
    for i in range(n):
        d = min(a[i], b[i])
        ans += d
        b[i] -= d
        e = min(a[i + 1], b[i])
        ans += e
        a[i + 1] -= e
    print(ans)


if __name__ == '__main__':
    n = int(input())
    a = np.fromstring(read(), dtype=np.int64, sep=' ')
    b = np.fromstring(read(), dtype=np.int64, sep=' ')
    main(n, a, b)
