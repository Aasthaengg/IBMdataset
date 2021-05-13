import heapq
n,m,*a = map(int,open(0).read().split())
a = list(map(lambda x: x*(-1), a))
heapq.heapify(a)
for _ in range(m):
  heapq.heappush(a,-(-heapq.heappop(a)//2))
print(-sum(a))