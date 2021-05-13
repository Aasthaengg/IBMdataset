import heapq
N, M = list(map(int,input().split()))
A = list(map(int,input().split()))
x = []
for i in range(N):
    heapq.heappush(x, -A[i])
for i in range(M):
    p = -heapq.heappop(x)
    heapq.heappush(x, -(p // 2))
ans = -sum(x)
print(ans)