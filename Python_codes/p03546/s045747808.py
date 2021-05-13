import sys, re
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop, heapify
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W = MAP()
c = [LIST() for _ in range(10)]
A = [LIST() for _ in range(H)]

#ワーシャルフロイド法  注意 PyPy非対応!!!!
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

graph = csr_matrix(c) #隣接行列からcsr行列をつくる
c = floyd_warshall(graph, directed=True) #有向の場合directed=True
#dist_matrixの中身はfloatになっているので注意！

#for i in range(10):
#	print(c[i])

ans = 0
for i in range(H):
	for x in A[i]:
		if x == 1 or x == -1:
			continue
		else:
			ans += c[x][1]

print(int(ans))

