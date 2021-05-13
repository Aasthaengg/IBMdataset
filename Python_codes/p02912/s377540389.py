import heapq

n,m=map(int,input().split())
a=[-int(x) for x in input().split()]
heapq.heapify(a)
for i in range(m):
  t=heapq.heappop(a)
  t=-t//2
  heapq.heappush(a,-t)
print(-sum(a))
