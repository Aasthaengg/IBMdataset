# -*- coding: utf-8 -*-
"""
B - Path
https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_b

"""
import sys


def solve(path):
    res = [0] * 5
    for a, b in path:
        res[a] += 1
        res[b] += 1
    res.sort()
    if res == [0, 1, 1, 2, 2]:
        return 'YES'
    return 'NO'


def main(args):
    path = [[int(i) for i in input().split()] for _ in range(3)]
    ans = solve(path)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
