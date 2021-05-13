import heapq
N = int(input())
V = list(map(int, input().split()))
heapq.heapify(V)
for i in range(N-1):
  v1 = heapq.heappop(V)
  v2 = heapq.heappop(V)
  heapq.heappush(V, (v1 + v2) / 2)
print(heapq.heappop(V))