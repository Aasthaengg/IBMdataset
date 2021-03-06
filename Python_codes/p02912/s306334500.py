from heapq import heapify, heappop, heappush
N, M = map(int, input().split())
a = [-int(a) for a in input().split()]
heapify(a)
for _ in range(M):
  heappush(a, int(heappop(a) / 2))
print(-sum(a))