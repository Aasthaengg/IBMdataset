# -*- coding: utf-8 -*-
"""
A - Regular Triangle
https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_a

"""
import sys


def solve(A, B, C):
    if A == B and B == C:
        return 'Yes'
    return 'No'


def main(args):
    A, B, C = map(int, input().split())
    ans = solve(A, B, C)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
