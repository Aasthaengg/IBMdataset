from numba import njit


@njit("UniTuple(i8, 3)(i8)")
def solve(N):
    for b in range(1, 3500 + 1):
        for c in range(1, 3500 + 1):
            num = N * b * c
            den = 4 * b * c - N * b - N * c
            if den > 0 and num % den == 0:
                a = num // den
                return a, b, c
    return 0, 0, 0


N = int(input())
print(*solve(N))

