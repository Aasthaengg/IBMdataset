N,M,*A=map(int,open(0).read().split())
from heapq import*
A=list(map(lambda x:-x,A))
heapify(A)
for _ in range(M):heappush(A,-(-heappop(A)//2))
print(-sum(A))
