n, m = map(int, input().split())
aas = list(map(int, input().split()))
import heapq
hq = []
for i in aas:
    heapq.heappush(hq,-i)
for i in range(m):
    tmp = heapq.heappop(hq)
    heapq.heappush(hq,-((-tmp)//2))
print(-sum(hq))