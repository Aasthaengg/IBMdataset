import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    S = input()

    cnt = 0
    for i in range(1, N):
        if (S[i - 1] == S[i]):
            cnt += 1

    print(min(cnt + 2 * K, N - 1))


if __name__ == '__main__':
    main()
