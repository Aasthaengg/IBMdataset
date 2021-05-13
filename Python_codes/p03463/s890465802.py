# -*- coding: utf-8 -*-
"""
A - Move and Win
https://atcoder.jp/contests/agc020/tasks/agc020_a

"""
import sys


def solve(N, A, B):
    if (A-B)%2:
        return 'Borys'
    return 'Alice'


def main(args):
    N, A, B = map(int, input().split())
    ans = solve(N, A, B)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
