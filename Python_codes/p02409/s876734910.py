# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_C&lang=jp

"""
import sys
from sys import stdin
input = stdin.readline


def solve(n):
    # ビルをつくる(どの部屋も入居者は0)
    buildings = []
    for _ in range(4):          #  ビルは4棟
        buildings.append([[0]*10 for _ in range(3)]) #  1フロア10部屋で3階建

    # 入居者の増減処理 (ビル番号、フロア番号、部屋番号が0起算になっているので、-1する)
    for _ in range(n):
        b, f, r, v = map(int, input().split())
        buildings[b-1][f-1][r-1] += v

    res = []
    for b in buildings:
        for f in b:
            f_stat = ' '.join(map(str, f))
            res.append(' ' + f_stat)
        res.append('#'*20)
    res = res[:-1]
    print(*res, sep='\n')


def main(args):
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main(sys.argv[1:])

