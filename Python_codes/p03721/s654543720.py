import heapq
n,k=map(int,input().split())

q=[]
for _ in range(n):
    a,b=map(int,input().split())
    heapq.heappush(q,(a,b))

while k>0:
    a,b=heapq.heappop(q)
    k-=b

print(a)