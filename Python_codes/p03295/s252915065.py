
n,m=map(int,input().split())
q=[]
import heapq
for i in range(m):
    a,b=map(int,input().split())
    heapq.heappush(q,(b,a))

largest=-10
c=0
while q:
    b,a=heapq.heappop(q)
    if largest-1<a:
        largest=b
        c+=1
print(c)
