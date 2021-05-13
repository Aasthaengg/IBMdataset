# -*- coding: utf-8 -*-
"""
B - Exchange
https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_b

"""
import sys


def solve(A, B, K):
    turn = 'takahashi'
    for _ in range(K):
        if turn == 'takahashi':
            A -= (A % 2)
            A //= 2
            B += A
            turn = 'aoki'
        else:
            B -= (B % 2)
            B //= 2
            A += B
            turn = 'takahashi'
    return A, B


def main(args):
    A, B, K = map(int, input().split())
    ans = solve(A, B, K)
    print(*ans)


if __name__ == '__main__':
    main(sys.argv[1:])