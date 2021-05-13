import heapq
n,m = map(int,input().split())
a = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(a)

for i in range(m):
    p = heapq.heappop(a)*(-1)
    p //= 2
    heapq.heappush(a,-p)
print(-sum(a))