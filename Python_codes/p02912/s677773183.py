from heapq import *
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=list(map(lambda x:x*(-1),a))
heapify(a)
for i in range(m):
    t=heappop(a)
    heappush(a,int(t/2))
print(-1*sum(a))