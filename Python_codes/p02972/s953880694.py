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

def get_divs(n):
	m = n**0.5
	divs = set()
	i = 1
	while i <= m:
		if n % i == 0:
			divs.add(i)
			divs.add(n//i)
		i += 1
	return divs

B = [0] * N

R = [0] * N
for i in range(N-1, -1, -1):
	if R[i] % 2 == A[i]:
		B[i] = 0
	else:
		B[i] = 1
		n = i+1
		for v in get_divs(n):
			R[v-1] += 1

ans = [i+1 for i, b in enumerate(B) if b == 1]
print(len(ans))
print(*ans)
