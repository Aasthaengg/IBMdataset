import sys
import numpy as np  # noqa
import numba  # noqa
from numba import njit, b1, i4, i8, f8  # noqa

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


@njit((i8, i8, i8[:]), cache=True)
def main(N, D, XY):
    count = 0
    for i in range(N):
        x, y = XY[i*2:i*2 + 2]
        if abs(x) > D or abs(y) > D:
            continue
        if x**2 + y ** 2 <= D**2:
            count += 1
    return count


N, D = map(int, readline().split())
XY = np.array(read().split(), np.int64)

print(main(N, D, XY))
