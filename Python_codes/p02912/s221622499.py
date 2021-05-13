import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [-v for v in a]
heapq.heapify(a)

for _ in range(m):
    x = heapq.heappop(a)
    heapq.heappush(a, (x+1)//2)

print(-sum(a))