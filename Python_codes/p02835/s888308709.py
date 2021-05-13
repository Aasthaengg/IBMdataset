# -*- coding: utf-8 -*-
"""
A - Blackjack
https://atcoder.jp/contests/abc147/tasks/abc147_a

"""
import sys


def solve(A):
    return 'win' if sum(A) <= 21 else 'bust'


def main(args):
    A = map(int, input().split())
    ans = solve(A)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
