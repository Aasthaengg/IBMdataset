import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x)*(-1), input().split()))

heapq.heapify(a)

for _ in range(m):
    # 一番高い商品に割引券を使って入れ直す
    a_max = -1 * heapq.heappop(a)
    a_max //= 2
    heapq.heappush(a, -a_max)

print(-sum(a))
