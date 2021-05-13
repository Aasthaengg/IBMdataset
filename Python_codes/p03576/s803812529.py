import sys
from bisect import bisect_left
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *XY = map(int, read().split())

    X = set()
    Y = set()
    for i, (x, y) in enumerate(zip(*[iter(XY)] * 2)):
        X.add(x)
        Y.add(y)

    X = sorted(X)
    Y = sorted(Y)

    P, Q = len(X), len(Y)

    ans = -1
    for i, x1 in enumerate(X):
        for x2 in X[i + 1 :]:
            for j, y1 in enumerate(Y):
                for y2 in Y[j + 1 :]:
                    p = 0
                    for x, y in zip(*[iter(XY)] * 2):
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            p += 1

                    if p >= K and (ans > (x2 - x1) * (y2 - y1) or ans == -1):
                        ans = (x2 - x1) * (y2 - y1)

    print(ans)
    return


if __name__ == '__main__':
    main()
