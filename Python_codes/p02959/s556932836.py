import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()
A = rl()
B = rl()

ans = 0
for i in range(N):
	for j in range(2):
		if A[i+j] >= B[i]:
			ans += B[i]
			A[i+j] -= B[i]
			B[i] = 0
		else:
			ans += A[i+j]
			B[i] = B[i] - A[i+j]
			A[i+j] = 0
print(ans)
