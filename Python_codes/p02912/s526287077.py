import heapq

n, m = map(int, input().split())
a = [ -int(x) for x in input().split()]
heapq.heapify(a)

for _ in range(m):
    cur = heapq.heappop(a)
    heapq.heappush(a, -(-cur//2))
print(-sum(a))