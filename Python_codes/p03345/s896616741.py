import heapq
from collections import defaultdict, deque
from math import ceil, factorial
from fractions import gcd
import sys

sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
smii = lambda: sorted(map(int, input().split()))


A, B, C, K = mii()

if K % 2:
    print(B - A)
else:
    print(A - B)
