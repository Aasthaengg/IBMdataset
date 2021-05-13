import sys

from numba import njit

input = sys.stdin.readline


@njit("Tuple((i8,i8,i8))(i8)")
def solve(N):
    for h in range(1, 3501):
        for n in range(1, 3501):
            a = N * h * n
            b = 4 * h * n - (h + n) * N
            if b > 0 and a % b == 0:
                w = a // b
                return h, n, w
    return -1, -1, -1


def main():
    N = int(input())
    h, n, w = solve(N)
    print(h, n, w)


if __name__ == "__main__":
    main()
