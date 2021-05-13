# -*- coding: utf-8 -*-
"""
A - Signboard
https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_a

"""
import sys


def solve(s):
    ans = 0
    for ch1, ch2 in zip(s, 'CODEFESTIVAL2016'):
        if ch1 != ch2:
            ans += 1
    return ans


def main(args):
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
