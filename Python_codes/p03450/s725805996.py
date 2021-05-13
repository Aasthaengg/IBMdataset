import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, M = MAP()
 
graph = defaultdict(list)
for _ in range(M):
	L, R, D = MAP()
	graph[L-1].append((R-1, D))
	graph[R-1].append((L-1, -D))
 
num = [None]*N

for i in range(N):
	if num[i] != None:
		continue
	q = deque([i])
	num[i] = 0
	while q:
		n = q.popleft()
		for node, weight in graph[n]:
			if num[node] == None:
				num[node] = num[n] + weight
				q.append(node)
			elif num[node] != num[n] + weight:
				print("No")
				exit()

else:
	print("Yes")