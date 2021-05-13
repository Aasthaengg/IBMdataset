# -*- coding: utf-8 -*-
"""
A - AKIBA
https://atcoder.jp/contests/cf17-final/tasks/cf17_final_a

"""
import sys


def solve(S):
    if 'AA' in S or 'KA' in S or 'IA' in S:
        return 'NO'
    if S.replace('A', '') == 'KIHBR':
        return 'YES'
    return 'NO'


def main(args):
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
