import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, x = map(int, input().split())
    A = list(map(int, input().split()))

    A_origin = A.copy()

    if A[0] > x:
        A[0] = x

    for i in range(0, N - 1):
        if A[i] + A[i + 1] > x:
            A[i + 1] -= A[i] + A[i + 1] - x

    res = 0
    for i in range(N):
        res += abs(A_origin[i] - A[i])

    print(res)


if __name__ == '__main__':
    main()
