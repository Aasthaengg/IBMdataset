import heapq
N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapq.heapify(A)

ans = 0
for i in range(M):
    most_expensive = -heapq.heappop(A)
    most_expensive //= 2
    heapq.heappush(A, -most_expensive)

print(-sum(A))
