# -*- coding: utf-8 -*-
"""
B - Golden Apple
https://atcoder.jp/contests/abc134/tasks/abc134_b

"""
import sys


def solve(N, D):
    ans = 1
    covered = D + 1 + D
    while covered < N:
        ans += 1
        covered += (2*D + 1)
    return ans


def main(args):
    N, D = map(int, input().split())
    ans = solve(N, D)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
