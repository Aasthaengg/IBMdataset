import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())

    num = [0 for _ in range(K)]
    for i in range(1, N + 1):
        num[i % K] += 1

    res = 0
    for a in range(0, K):
        b = (K - a) % K
        c = (K - a) % K
        if (b + c) % K != 0:
            continue
        res += num[a] * num[b] * num[c]

    print(res)


if __name__ == '__main__':
    main()
