# -*- coding: utf-8 -*-
"""
B - Strings with the Same Length
https://atcoder.jp/contests/abc148/tasks/abc148_b

"""
import sys


def solve(S, T):
    return ''.join(s+t for s, t in zip(S, T))


def main(args):
    _ = input()
    S, T = input().split()
    ans = solve(S, T)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
