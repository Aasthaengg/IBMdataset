import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    cntB = [0 for _ in range(N)]
    for i, b in enumerate(B):
        cntB[i] = N - bisect.bisect_right(C, b)

    cumsumB = [0 for _ in range(N)]
    cumsumB[-1] = cntB[-1]
    for i in range(N - 2, -1, -1):
        cumsumB[i] = cumsumB[i + 1] + cntB[i]

    res = 0
    for i, a in enumerate(A):
        idx = bisect.bisect_right(B, a)
        if idx < N:
            res += cumsumB[idx]

    print(res)


if __name__ == '__main__':
    main()
