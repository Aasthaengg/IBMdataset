import sys
from io import StringIO
import unittest


def resolve():
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    n, k = list(map(int, input().split()))
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    L = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    Lsort = sorted(L, reverse=True)
    re = 0
    for i in range(k):
        re += Lsort[i]

    print(re)
resolve()