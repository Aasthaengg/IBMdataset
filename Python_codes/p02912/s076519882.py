import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [-i for i in a]
heapq.heapify(a)

for i in range(m):
    p = heapq.heappop(a)*(-1)
    p //= 2
    heapq.heappush(a, -p)

print(-sum(a))