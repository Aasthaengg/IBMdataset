from heapq import heapify, heappop, heappush
N, M = map(int, input().split())
*A, = map(lambda x: -int(x), input().split())
heapify(A)
for _ in range(M):
    x = heappop(A)
    x = -(-x//2)
    heappush(A, x)
print(-sum(A))