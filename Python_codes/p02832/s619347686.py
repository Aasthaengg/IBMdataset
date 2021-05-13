# -*- coding: utf-8 -*-
"""
D - Brick Break
https://atcoder.jp/contests/abc148/tasks/abc148_d

"""
import sys


def solve(N, arr):
    x = 1
    last = -1
    ans = 0
    for a in arr:
        if a != x:
            ans += 1
        else:
            x += 1
            last = 1
    return ans if last != -1 else -1


def main(args):
    N = int(input())
    arr = [int(a) for a in input().split()]
    ans = solve(N, arr)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
