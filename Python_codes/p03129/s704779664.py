# -*- coding: utf-8 -*-
"""
A - Anti-Adjacency
https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a

"""
import sys


def solve(N, K):
    if (N+1) //2 >= K:
        return 'YES'
    return 'NO'


def main(args):
    N, K = map(int, input().split())
    ans = solve(N, K)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
