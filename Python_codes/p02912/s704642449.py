import heapq
N,M = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    A[i] = -A[i]
heapq.heapify(A)

for i in range(M):
    trgt = -heapq.heappop(A)//2
    heapq.heappush(A,-trgt)
print(-sum(A))