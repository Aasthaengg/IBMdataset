# -*- coding: utf-8 -*-
"""
D - ModSum
https://atcoder.jp/contests/abc139/tasks/abc139_d

"""
import sys


def solve(N):
    return (1 + (N-1)) * (N - 1) // 2


def main(args):
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
