import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
A, B = [], []
for i in range(N):
    a, b = MAP()
    A.append(a)
    B.append(b)

cnt = 0
for i in range(1, N+1):
    if (A[N-i] + cnt) % B[N-i] != 0:
        cnt += B[N-i] - (A[N-i] + cnt) % B[N-i]
print(cnt)
