import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    H, W, A, B = map(int, input().split())

    res = []
    for _ in range(B):
        row = [0 for _ in range(W)]
        for i in range(A, W):
            row[i] = 1
        res.append(row)

    for _ in range(H - B):
        row = [0 for _ in range(W)]
        for i in range(A):
            row[i] = 1
        res.append(row)

    for re in res:
        re = [str(r) for r in re]
        print(''.join(re))


if __name__ == '__main__':
    main()
