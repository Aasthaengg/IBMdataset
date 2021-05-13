# -*- coding: utf-8 -*-
"""
A - Measure
https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_a

"""
import sys


def solve(S):
    return S if len(S) == 2 else S[::-1]


def main(args):
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])