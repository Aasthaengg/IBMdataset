from heapq import *

n,m=map(int,input().split())
a=list(map(lambda x:int(x)*-1,input().split()))

heapify(a)

for i in range(m):
    x=heappop(a)
    x*=-1
    x//=2
    x*=-1
    heappush(a,x)


print(sum(a)*-1)