# -*- coding: utf-8 -*-
"""
B - Greedy Takahashi
https://atcoder.jp/contests/abc149/tasks/abc149_b

"""
import sys


def solve(A, B, K):
    if A >= K:
        return A-K, B
    return 0, max(B - K + A, 0)


def main(args):
    A, B, K = map(int, input().split())
    ans = solve(A, B, K)
    print(*ans)


if __name__ == '__main__':
    main(sys.argv[1:])
