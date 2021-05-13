import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)

    print("second" if all(A[i] % 2 == 0 for i in range(N)) else "first")


if __name__ == '__main__':
    main()
