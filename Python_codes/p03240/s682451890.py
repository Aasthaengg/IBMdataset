import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    X = []
    Y = []
    H = []
    si = -1
    for i in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
        if h > 0:
            si = i

    for cx in range(0, 101):
        for cy in range(0, 101):
            h = H[si] + abs(X[si] - cx) + abs(Y[si] - cy)
            ok = True
            for i in range(N):
                if H[i] != max(h - abs(X[i] - cx) - abs(Y[i] - cy), 0):
                    ok = False
                    break
            if ok:
                return print(cx, cy, h)


if __name__ == '__main__':
    main()
