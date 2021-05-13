from numba import njit


@njit
def solve(N):
    for b in range(1, 3500 + 1):
        for c in range(1, 3500 + 1):
            num = N * b * c
            den = 4 * b * c - N * b - N * c
            if den > 0 and num % den == 0:
                return num // den, b, c


N = int(input())
print(*solve(N))
