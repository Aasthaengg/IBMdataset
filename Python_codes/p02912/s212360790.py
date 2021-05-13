
from heapq import heappop, heappush

N, M = map(int, input().split())
X = list(map(int, input().split()))

pq = []
for v in X:
    heappush(pq, -v)

for _ in range(M):
    u = heappop(pq)
    heappush(pq, -(-u // 2))

print(-sum(pq))
