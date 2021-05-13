import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    V = []
    for a, b in zip(A, B):
        V.append((a + b, a, b))

    V.sort(reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if i % 2 == 0:
            takahashi += V[i][1]
        else:
            aoki += V[i][2]

    print(takahashi - aoki)


if __name__ == '__main__':
    main()
