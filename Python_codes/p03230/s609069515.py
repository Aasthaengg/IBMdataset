import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby
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
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
k = int(0.5+(2*N)**0.5)
if k*(k+1) == 2*N:  # 集合の数がk+1, サイズがk
	print("Yes")
	print(k+1)
	ans = [[] for _ in range(k+1)]
	for i, (x, y) in enumerate(combinations(range(k+1), 2)):
		ans[x].append(i+1)
		ans[y].append(i+1)
	for l in ans:
		print(k, *l)
else:
	print("No")
