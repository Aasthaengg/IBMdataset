import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N = ri()
V = rl()

import heapq

heap = []
for v in V:
	heapq.heappush(heap, v)

while len(heap) >= 2:
	v = heapq.heappop(heap)
	v2 = heapq.heappop(heap)
	nv =(v + v2)/2
	heapq.heappush(heap, nv)
print(heap[0])
