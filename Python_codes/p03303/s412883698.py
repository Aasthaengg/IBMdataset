# -*- coding: utf-8 -*-
"""
B - Acrostic
https://beta.atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_b

"""
import sys
from sys import stdin
input = stdin.readline


def main(args):
    S = input().strip()
    w = int(input())
    ans = [S[i] for i in range(0, len(S), w)]
    print(''.join(ans))


if __name__ == '__main__':
    main(sys.argv[1:])
