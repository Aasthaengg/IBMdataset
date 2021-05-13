# -*- coding: utf-8 -*-
"""
E - Double Factorial
https://atcoder.jp/contests/abc148/tasks/abc148_e

"""
import sys


def solve(N):
    if N % 2:
        return 0
    ans, d = 0, 10
    while True:
        q = N // d
        ans += q
        if q == 0:
            return ans
        d *= 5


def main(args):
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
