import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()
A = []
for i in range(N):
	A.append(ri())
m = max(A)
if len([a for a in A if a == m]) > 1:
	for i in range(N):
		print(m)
else:
	m2 = -1
	i2 = -1
	for i, a in enumerate(A):
		if a == m:
			continue
		if m2 < a:
			m2 = a
			i2 = i
	for a in A:
		if a == m:
			print(m2)
		else:
			print(m)
