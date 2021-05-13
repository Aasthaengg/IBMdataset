import heapq

n,m=map(int,input().split())
*a,=map(int,input().split())

q=[]
for aa in a:
    heapq.heappush(q,-aa)

while m>0:
    aa=heapq.heappop(q)
    heapq.heappush(q,-((-aa)//2))
    m-=1

print(-sum(q))