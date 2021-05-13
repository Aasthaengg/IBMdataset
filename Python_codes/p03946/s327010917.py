import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, T = MAP()
A = LIST()

lis = []
tmp = A[0]
tmp_max = 0
for i in range(N):
	if tmp > A[i]:
		tmp = A[i]
		lis.append(tmp_max)
		tmp_max = 0
	else:
		tmp_max = max(tmp_max, A[i]-tmp)
lis.append(tmp_max)

print(lis.count(max(lis)))
