import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N, M = rl()
A = []
Cs = []
for i in range(M):
	a, b = rl()
	C = rl()
	A.append(a)
	Cs.append(C)

def get_bit(C):
	b = 0
	for c in C:
		b = b | (1 << (c-1))
	return b
bits =[]
for C in Cs:
	b = get_bit(C)
	bits.append(b)

start = 0
end = 2**N-1

import heapq

heap = []
heapq.heappush(heap, (0, start))

visited = {}
ans = -1
while heap:
	c, n = heapq.heappop(heap)
	if n == end:
		ans = c
		break
	for i, b in enumerate(bits):
		m = n | b
		nc = c + A[i]
		if m in visited and nc >= visited[m]:
			continue
		visited[m] = nc
		heapq.heappush(heap, (nc, m))
print(ans)
