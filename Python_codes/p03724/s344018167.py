import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    cnt = [0 for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        cnt[a] += 1
        cnt[b] += 1

    for c in cnt:
        if c % 2 != 0:
            return print("NO")

    print("YES")


if __name__ == '__main__':
    main()
