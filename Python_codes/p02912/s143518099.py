import heapq
N,M = map(int,input().split())
A = list(map(int,input().split()))
q = []
for i in A:
    heapq.heappush(q, -i)

for i in range(M):
    expe = heapq.heappop(q)
    expe = -expe // 2
    heapq.heappush(q, -expe)
print(-sum(q))