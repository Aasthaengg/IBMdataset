import heapq
import math
n,m=map(int, input().split())
hp=list(map(lambda x:-1*int(x), input().split()))
heapq.heapify(hp)
for _ in range(m):
  item=heapq.heappop(hp)
  heapq.heappush(hp, math.ceil(item/2))
  
print(sum(hp)*-1)
