# -*- coding: utf-8 -*-
"""
A - B +/- A
https://atcoder.jp/contests/abc118/tasks/abc118_a

"""
import sys


def main(args):
    A, B = map(int, input().split())
    ans = A + B if B % A == 0 else B - A
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
