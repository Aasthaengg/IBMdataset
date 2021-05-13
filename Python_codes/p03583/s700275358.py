from numba import njit

N = int(input())


@njit
def f():
    for h in range(1, 3501):
        for n in range(1, 3501):
            x = 4 * h * n - N * n - N * h
            if x != 0 and N * h * n % x == 0:
                w = N * h * n // x
                if w >= 1:
                    return h, n, w


print(*f())
