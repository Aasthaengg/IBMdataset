import heapq
N=int(input())
v=list(map(int,input().split()))
heapq.heapify(v)
for x in range(N-1):
  t1=heapq.heappop(v)
  t2=heapq.heappop(v)
  heapq.heappush(v,(t1+t2)/2)
print(heapq.heappop(v))