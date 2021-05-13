import heapq
import math

n,m=map(int,input().split())
aa=list(map(int,input().split()))
a=[i*(-1) for i in aa]
heapq.heapify(a)

for i in range(m):
    high=heapq.heappop(a)
    heapq.heappush(a,-math.floor(-high/2))

print(-sum(a))
