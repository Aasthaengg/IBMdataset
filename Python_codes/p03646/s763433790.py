import sys, math, itertools, bisect, copy, re, heapq
from collections import Counter, deque, defaultdict
from itertools import accumulate, permutations, combinations, takewhile, compress, cycle

# from functools import reduce
# from math import ceil, floor, log10, log2, factorial
# from pprint import pprint


INF = float('inf')
MOD = 10 ** 9 + 7
EPS = 10 ** -7
sys.setrecursionlimit(1000000)

# N = int(input())
# N,M = [int(x) for x in input().split()]
# V = [[0] * 100 for _ in range(100)]
# A = [int(input()) for _ in range(N)]
# DP = [[0] * 100 for _ in range(100)]
# DP = defaultdict(lambda: float('inf'))

K = int(input())

MAX = 10 ** 16


def f(i, j):
    P = K % 50
    Q = i // 50
    if j < P:
        ret = 49 + 50 - P + 1 + Q
    else:
        ret = 49 - P + Q
    return ret


A = []
for j in range(50):
    A.append(f(K, j))

# print(A)
print(50)
print(" ".join([str(x) for x in A]))