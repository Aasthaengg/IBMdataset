from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from heapq import heappop, heappush, heappushpop
import copy
import numpy as np
import sys
INF = float('inf')
mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)

# 1 2 3
# a, b, c = LI()


def LI(): return list(map(int, sys.stdin.buffer.readline().rsplit()))

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


n, q = LI()
point = [0]*n
graph = [[] for i in range(n)]
visited = [False]*n


def dfs(n):
    visited[n-1] = True
    for node in graph[n-1]:
        if visited[node-1]:
            continue
        point[node-1] += point[n-1]
        dfs(node)


def main():

    for i in range(n - 1):
        a, b = LI()
        graph[a - 1].append(b)
        graph[b - 1].append(a)

    for i in range(q):
        p, x = LI()
        point[p - 1] += x

    dfs(1)

    print(*point)


if __name__ == "__main__":
    main()
