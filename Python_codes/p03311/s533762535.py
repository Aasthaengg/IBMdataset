import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = [a - (i + 1) for i, a in enumerate(A)]
    A.sort()
    b = A[(N + 1) // 2 - 1]

    res = 0
    for a in A:
        res += abs(a - b)

    print(res)


if __name__ == '__main__':
    main()
