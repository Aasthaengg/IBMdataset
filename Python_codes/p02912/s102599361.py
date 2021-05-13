import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x * (-1), A))
heapq.heapify(A)

for _ in range(M):
    tmp = heapq.heappop(A) * (-1)
    tmp //= 2
    heapq.heappush(A, tmp * (-1))

print(-sum(A))
