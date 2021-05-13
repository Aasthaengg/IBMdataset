# -*- coding: utf-8 -*-
"""
D - AtCoDeerくんと変なじゃんけん / AtCoDeer and Rock-Paper
https://atcoder.jp/contests/arc062/tasks/arc062_b

"""
import sys


def solve(s):
    rock, paper = 0, 0
    ans = 0
    for h in s:
        if rock > paper:
            paper += 1
            if h == 'g':
                ans += 1
        else:
            rock += 1
            if h == 'p':
                ans -=1
    return ans


def main(args):
    s = input()
    ans = solve(s)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])