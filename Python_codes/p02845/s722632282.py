import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    A = list(map(int, input().split()))

    MOD = 1000000007

    res = 1
    cnt = {'R': 0, 'G': 0, 'B': 0}
    for a in A:
        cv = 0
        cc = 'R'
        for c, v in cnt.items():
            if v == a:
                cv += 1
                cc = c
        res *= cv
        res %= MOD
        cnt[cc] += 1

    print(res)


if __name__ == '__main__':
    main()
