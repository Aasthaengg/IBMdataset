from heapq import heapify, heappop, heappush
N, M = map(int, input().split())
A = [-a for a in list(map(int, input().split()))]
heapify(A)
for _ in range(M):
  p = heappop(A)
  heappush(A, -((-p)//2))
print(-sum(A))