# -*- coding: utf-8 -*-
"""
B - Red or Blue
https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_b

"""
import sys


def solve(s):
    red = s.count('R')
    blue = s.count('B')
    if red > blue:
        return 'Yes'
    return 'No'


def main(args):
    _ = int(input())
    s = input()
    ans = solve(s)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
