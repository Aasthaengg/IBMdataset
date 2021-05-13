# -*- coding: utf-8 -*-
"""
A - Colorful Slimes 2
https://atcoder.jp/contests/agc026/tasks/agc026_a

"""
import sys


def solve(N, slimes):
    prev = None
    ans = 0
    for s in slimes:
        if s == prev:
            prev = None
            ans += 1
        else:
            prev = s
    return ans


def main(args):
    N = int(input())
    slimes = [int(a) for a in input().split()]
    ans = solve(N, slimes)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
