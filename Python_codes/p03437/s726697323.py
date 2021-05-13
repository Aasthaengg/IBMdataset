# -*- coding: utf-8 -*-
"""
A - Two Integers
https://atcoder.jp/contests/apc001/tasks/apc001_a

"""
import sys


def solve(X, Y):
    t = X / Y
    if t.is_integer():
        return -1
    return X


def main(args):
    X, Y = map(int, input().split())
    ans = solve(X, Y)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
