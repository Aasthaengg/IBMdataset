import heapq 

N,M=map(int,input().split())
A=[-a for a in list(map(int,input().split()))]
heapq.heapify(A)
for _ in [0]*M:
    a=heapq.heappop(A)
    heapq.heappush(A,-((-a)//2))
    
res=0
for i in range(N):
    a=heapq.heappop(A)
    res+=-a
print(res)