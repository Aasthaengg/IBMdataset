import heapq

n, m = map(int, input().split())
an = list(map(int, input().split()))

an = [-1 * i for i in an]

heapq.heapify(an)

for _ in range(m):
    x = heapq.heappop(an)
    x = int(x/2)
    heapq.heappush(an, x)

print(-1 * sum(an))