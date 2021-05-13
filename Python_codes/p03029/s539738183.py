import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1


A, P = map(int, input().split())
print((A * 3 + P) // 2)
