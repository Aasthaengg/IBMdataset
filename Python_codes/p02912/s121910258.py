import heapq
n, m = map(int, input().split())
A = sorted(map(lambda x: -int(x), input().split()))
for _ in range(m):
    a = heapq.heappop(A)
    a = -(-a//2)
    heapq.heappush(A, a)

print(-sum(A))
