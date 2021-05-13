#!/usr/bin python3
# -*- coding: utf-8 -*-

# ワーシャルフロイド法
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数

from scipy.sparse.csgraph import floyd_warshall
from collections import Counter

def main():
    H, W = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(10)]
    fw=floyd_warshall(d)
    p = []
    for i in range(H):
        p+=list(map(int,input().split()))
    p = Counter(p)
    ret = 0
    for i in range(10):
        if i==1: continue
        ret += p[i]*fw[i][1]
    print(int(ret))


if __name__ == '__main__':
    main()