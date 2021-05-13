# -*- coding: utf-8 -*-
"""
A - Curtain
https://atcoder.jp/contests/abc143/tasks/abc143_a

"""
import sys


def solve(A, B):
    return max(0, A - B * 2)


def main(args):
    A, B = map(int, input().split())
    ans = solve(A, B)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
