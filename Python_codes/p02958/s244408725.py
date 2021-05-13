import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()
P = rl()

import itertools

def check(P):
	#print(P)
	prev = P[0]
	for i in range(1, len(P)):
		if prev > P[i]:
			return False
		prev = P[i]
	return True

P0 = list(P)
if check(P):
	print('YES')
	exit()
for c in itertools.combinations(list(range(N)), 2):
	i, j = c
	#print(i, j)
	P = list(P0)
	P[i], P[j] = P[j], P[i]
	if check(P):
		print('YES')
		exit()
print('NO')