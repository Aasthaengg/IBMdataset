# -*- coding: utf-8 -*-
"""
A - ABC/ARC
https://atcoder.jp/contests/abc053/tasks/abc053_a

"""
import sys


def solve(x):
    if x < 1200:
        return 'ABC'
    return 'ARC'


def main(args):
    x = int(input())
    ans = solve(x)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])