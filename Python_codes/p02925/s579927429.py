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
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
	N = INT()
	A = [LIST() for _ in range(N)]

	graph_out = defaultdict(list)
	graph_in = defaultdict(list)
	match_id = [[0]*N for _ in range(N)]

	def toid(i, j):  # 選手から試合IDに変換
		if i > j: i, j = j, i
		return match_id[i][j]

	cnt = 0
	for i in range(N):
		for j in range(N):
			if i < j:
				match_id[i][j] = cnt
				cnt += 1

	V = N*(N-1)//2
	gout = [[] for _ in range(V)]
	gin = [[] for _ in range(V)]
	deg = [0]*(V)
	for i in range(N):
		for j in range(N-2):
			gout[toid(i, A[i][j]-1)].append(toid(i, A[i][j+1]-1))
			deg[toid(i, A[i][j+1]-1)] += 1
			gin[toid(i, A[i][j+1]-1)].append(toid(i, A[i][j]-1))
	# トポロジカルソート
	ans = [v for v in range(V) if deg[v]==0]
	deq = deque(ans)
	used = [0]*V
	while deq:
	    v = deq.popleft()
	    for t in gout[v]:
	        deg[t] -= 1
	        if deg[t]==0:
	            deq.append(t)
	            ans.append(t)
	if any(deg):
		print(-1)
		exit()

	cnt = [0]*V  # cntが入り次数に達したら発火
	day = [0]*V
	q = deque(ans)
	ans = 0

	while q:
		n = q.popleft()
		for node in gout[n]:
			cnt[node] += 1
			if cnt[node] == len(gin[node]):
				q.append(node)
				day[node] = day[n] + 1
				ans = day[node]
	print(ans+1) 

if __name__ == '__main__':
	main()
