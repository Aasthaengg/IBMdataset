import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    if N == 1:
        return print(1)

    X = [0 for _ in range(N)]
    Y = [0 for _ in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = x
        Y[i] = y

    cnt = {}
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            rx = X[i] - X[j]
            ry = Y[i] - Y[j]
            if (rx, ry) not in cnt:
                cnt[(rx, ry)] = 1
            else:
                cnt[(rx, ry)] += 1
            if (-rx, -ry) not in cnt:
                cnt[(-rx, -ry)] = 1
            else:
                cnt[(-rx, -ry)] += 1

    cnt = [[v, k] for k, v in cnt.items()]
    cnt.sort(reverse=True)
    res = N - cnt[0][0] // 2
    print(res)


if __name__ == '__main__':
    main()
