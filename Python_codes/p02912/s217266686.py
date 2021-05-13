from heapq import heappush, heappop

N, M = map(int, input().split())
*A, = map(int, input().split())
q = []
for i in A:
    heappush(q, -i)

for _ in range(M):
    a = -heappop(q)
    heappush(q, -(a//2))
print(-sum(q))