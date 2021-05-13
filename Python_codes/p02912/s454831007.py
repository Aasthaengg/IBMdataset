import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range (0, N):
	A[i] = -1*A[i]

A = sorted(A)

heapq.heapify(A)

import math

for i in range (0, M):
	V = heapq.heappop(A)
	V = math.ceil(V/2)
	heapq.heappush(A, V)
  
print(-1*sum(A))