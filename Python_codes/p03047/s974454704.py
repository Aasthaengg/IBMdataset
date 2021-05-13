# -*- coding: utf-8 -*-
"""
A - Consecutive Integers
https://atcoder.jp/contests/diverta2019/tasks/diverta2019_a

"""
import sys


def solve(N, K):
    return N-K+1


def main(args):
    N, K = map(int, input().split())
    ans = solve(N, K)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
