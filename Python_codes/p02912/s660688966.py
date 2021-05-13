from heapq import heappush, heappop

N, M, *A = map(int, open(0).read().split())

q = []
for v in A:
    heappush(q, -v)
    
for _ in range(M):
    v = heappop(q)
    heappush(q, -((-v) // 2))
    
print(-sum(q))
