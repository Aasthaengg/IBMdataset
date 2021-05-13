import heapq

N,M=map(int,input().split())
A=list(map(int,input().split()))

for i in range(0,N):
    A[i]=-A[i]

heapq.heapify(A)
for i in range(0,M):
    x=heapq.heappop(A)
    x=-x
    x=x//2
    heapq.heappush(A,-x)

ans=0
for i in range(0,N):
    ans-=A[i]
print(ans)
