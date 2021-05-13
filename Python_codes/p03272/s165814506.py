# -*- coding: utf-8 -*-
"""
A - Train
https://atcoder.jp/contests/abc107/tasks/abc107_a

"""
import sys


def solve(N, i):
    return N - i + 1


def main(args):
    N, i = map(int, input().split())
    ans = solve(N, i)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
