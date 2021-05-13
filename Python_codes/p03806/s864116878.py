# -*- coding: utf-8 -*-
"""
D - Mixing Experiment
https://atcoder.jp/contests/abc054/tasks/abc054_d

"""
import sys


def solve(N, Ma, Mb, items):
    d = dict()
    d[(0, 0)] = 0
    for a, b, c in items:
        nd = dict()
        for k, v in d.items():
            t = d.get((k[0], k[1]), float('inf')) + c
            if d.get((k[0]+a, k[1]+b), float('inf')) > t:
                nd[(k[0]+a, k[1]+b)] = t
        d.update(nd)
    res = []
    for k, v in d.items():
        if k == (0, 0):
            continue
        a, b = k
        if a*Mb == b*Ma:
            res.append(v)
    return min(res) if res else -1


def main(args):
    N, Ma, Mb = map(int, input().split())
    items = [[int(i) for i in input().split()] for _ in range(N)]
    ans = solve(N, Ma, Mb, items)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
