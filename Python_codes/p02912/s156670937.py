n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
  a[i]=a[i]*-1
import heapq
heapq.heapify(a)
for i in range(m):
  t=(heapq.heappop(a))*-1
  heapq.heappush(a,(t//2)*-1)
print(sum(a)*-1)