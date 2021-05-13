
import numba  # noqa
from numba import njit, b1, i4, i8, f8  # noqa

N = int(input())


@njit((i8, ), cache=True)
def main(N):
    ans = 0
    for j in range(1, N + 1):
        x = N // j
        ans += int(j * x * (x + 1) / 2)
    return ans


print(main(N))
