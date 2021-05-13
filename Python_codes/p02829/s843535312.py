# -*- coding: utf-8 -*-
"""
A - Round One
https://atcoder.jp/contests/abc148/tasks/abc148_a

"""
import sys


def solve(A, B):
    return set([1, 2, 3]) - set([A, B])


def main(args):
    A, B = int(input()), int(input())
    ans = solve(A, B)
    print(*ans)


if __name__ == '__main__':
    main(sys.argv[1:])
