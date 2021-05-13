# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from heapq import heappop, heappush, heappushpop, heapify
import copy
import numpy as np
import sys
INF = float('inf')
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)

# 1 2 3
# a, b, c = LI()


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))

# a = I()


def I(): return int(sys.stdin.buffer.readline())

# abc def
# a, b = LS()


def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

# a = S()


def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')

# 2
# 1
# 2
# [1, 2]


def IR(n): return [I() for i in range(n)]

# 2
# 1 2 3
# 4 5 6
# [[1,2,3], [4,5,6]]


def LIR(n): return [LI() for i in range(n)]

# 2
# abc
# def
# [abc, def]


def SR(n): return [S() for i in range(n)]

# 2
# abc def
# ghi jkl
# [[abc,def], [ghi,jkl]]


def LSR(n): return [LS() for i in range(n)]

# 2
# abcd
# efgh
# [[a,b,c,d], [e,f,g,h]]


def SRL(n): return [list(S()) for i in range(n)]


def main():
    n, m = LI()
    a = sorted(list(LI()))
    # 1. c以下をcに毎回置き換え.
    # for i in range(m):
    #     b, c = LI()
    #     for j in range(b):
    #         if a[j] > c:
    #             break
    #         heappushpop(a, c)
    # print(sum(a))

    # 2. 大きいcから入れていってbの累計がlen(a)になったら即終わり.
    # bc = LIR(m)
    # bc.sort(key=lambda x: x[1])
    # cnt = 0
    # for pair in bc:
    #     heappushpop(a, pair[1])
    #     cnt += pair[0]
    #     if cnt > len(a):
    #         break
    # print(sum(a))

    bc = LIR(m)
    bc.sort(key=lambda x: x[1], reverse=True)
    d = []
    i = 0
    while len(d) < n and i < len(bc):
        if bc[i][0] + len(d) < n:
            d.extend([bc[i][1]] * bc[i][0])
        else:
            d.extend([bc[i][1]] * (n - len(d)))
            break
        i += 1
    for i in range(len(d)):
        if d[i] < a[i]:
            break
        a[i] = d[i]
    print(sum(a))


if __name__ == "__main__":
    main()
