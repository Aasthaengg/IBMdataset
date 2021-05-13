# -*- coding: utf-8 -*-
"""
B - Palindrome-philia
https://atcoder.jp/contests/abc147/tasks/abc147_b

"""
import sys


def solve(S):
    l, r = 0, len(S) - 1
    ans = 0
    while l < r:
        ans += (S[l] != S[r])
        l += 1
        r -= 1
    return ans


def main(args):
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
