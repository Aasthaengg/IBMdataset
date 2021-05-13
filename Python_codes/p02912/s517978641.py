inp=list(map(int,input().split()))
m=inp[1]
inp=list(map(int,input().split()))
ans=0
inp=[-1*item for item in inp]
import heapq
heapq.heapify(inp)
while m>0:
    a=heapq.heappop(inp)
    a*=-1
    x=a//2
    heapq.heappush(inp,-1*x)
    m-=1
print (-1*sum(inp))