# -*- coding: utf-8 -*-
"""
A - Red or Not
https://atcoder.jp/contests/abc138/tasks/abc138_a

"""
import sys


def solve(a, s):
    return s if a >= 3200 else 'red'


def main(args):
    a = int(input())
    s = input()
    ans = solve(a, s)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
