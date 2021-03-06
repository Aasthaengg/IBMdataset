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
ab = [LIST() for _ in range(N-1)]
c = LIST()
c.sort(reverse=True)
tree = [[] for _ in range(N)]
for a, b in ab:
	tree[a-1].append(b-1)
	tree[b-1].append(a-1)

start=None
for i in range(N):
	if len(tree[i]) == 1:
		start = i
		break

ans = [0]*N
q = deque()
q.append(start)
ans[start] = c[0]
cnt = 1
while q:
	n = q.popleft()
	for node in tree[n]:
		if ans[node]:
			continue
		ans[node] = c[cnt]
		cnt += 1
		q.append(node)
print(sum(c)-max(c))
print(*ans)
