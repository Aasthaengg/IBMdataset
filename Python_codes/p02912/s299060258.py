import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [x*(-1) for x in a]
heapq.heapify(a)

for i in range(m):
    c = (heapq.heappop(a)*(-1)//2)*(-1)
    heapq.heappush(a, c)
print(-sum(a))

