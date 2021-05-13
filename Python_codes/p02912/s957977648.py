import heapq
N, M = map(int,input().split())
al = list(map(int,input().split()))
al = list(map(lambda x: x*(-1), al))
heapq.heapify(al)

for _ in range(M):
    tmp_min = heapq.heappop(al)
    heapq.heappush(al, -1*(-tmp_min//2))
print(-sum(al))