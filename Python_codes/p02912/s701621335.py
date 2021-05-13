import heapq
N, M = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x*(-1), a))
heapq.heapify(a)

for _ in range(M):
  X = heapq.heappop(a)
  heapq.heappush(a, X/2)

print(sum(int(-x) for x in a))