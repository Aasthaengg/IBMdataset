
import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-A[i] for i in range(N)]
ans = 0
heapq.heapify(A)
for i in range(M):
    value = -heapq.heappop(A)
    value //= 2
    heapq.heappush(A, -value)
print(-sum(A))