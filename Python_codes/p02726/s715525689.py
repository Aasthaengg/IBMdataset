from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from heapq import heappop, heappush, heappushpop
import copy
import numpy as np
import sys
INF = float('inf')
mod = 10**9+7


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
    n, x, y = LI()
    d = [0]*n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            d[min(j - i, abs(x - i) + 1 + abs(j - y)) - 1] += 1
    for k in range(n-1):
        print(d[k])


if __name__ == "__main__":
    main()
