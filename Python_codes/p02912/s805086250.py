import heapq
N,M = map(int,input().split())
A = list(map(int,input().split()))
heap = []
for i in range(N):
    heapq.heappush(heap,-A[i])
for _ in range(M):
    a = heapq.heappop(heap)
    a = -a
    a = a//2
    heapq.heappush(heap,-a)
print(-sum(heap))