from heapq import heappush,heappop
n,k=map(int,input().split())
a=list(map(int,input().split()))
q=[]
for i in a:
  heappush(q,-i)
for _ in range(k):
  i=heappop(q)
  i=-i//2
  heappush(q,-i)
print(-sum(q))