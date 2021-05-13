import heapq as hp

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] * (-1)
hp.heapify(a)

for _ in range(m):
    max_price = (-1) * hp.heappop(a)
    hp.heappush(a, (-1) * (max_price // 2))

print(-sum(a))