N,M=map(int,input().split())
*A,=map(int,input().split())
from heapq import*
B=[]
for a in A:
    B.append(-a)
heapify(B)
for i in range(M):
    b=heappop(B)
    b=0--b//2
    heappush(B,b)
print(-sum(B))