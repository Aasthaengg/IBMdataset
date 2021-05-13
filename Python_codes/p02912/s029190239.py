from heapq import *
N,M = map(int,input().split())
A = list(map(lambda x: -int(x),input().split()))
heapify(A)
for i in range(M):
    heappush(A,-(-heappop(A)//2))
print(-sum(A))