import heapq

N, M = map(int, input().split())
A = list(map(lambda x: int(x)*(-1), input().split()))

heapq.heapify(A)

for _ in range(M):
  v = heapq.heappop(A) * (-1)
  heapq.heappush(A, -(v >> 1))

print(-sum(A))