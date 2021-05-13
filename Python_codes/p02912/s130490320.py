from heapq import heappop,heappush

n,m=map(int,input().split())
a=list(map(int,input().split()))

h=[]
for l in a:
    heappush(h,-l) 
    
for i in range(m):
    amax=heappop(h)
    l=(-amax)//2
    heappush(h,-l)
    
print(-sum(h))
