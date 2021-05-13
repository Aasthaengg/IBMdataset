# -*- coding: utf-8 -*-
"""
A - Circle
https://atcoder.jp/contests/abc145/tasks/abc145_a

"""
import sys


def solve(r):
    return r ** 2


def main(args):
    r = int(input())
    ans = solve(r)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
