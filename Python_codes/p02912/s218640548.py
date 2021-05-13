import heapq
n, m, *a = map(int, open(0).read().split())
a = list(map(lambda x: -x, a))

heapq.heapify(a)
for i in range(m):
    b = -heapq.heappop(a)
    heapq.heappush(a, -(b >> 1))

print(-sum(a))
