from heapq import heapify, heappush, heappop
n, m = map(int, input().split())
a = list(map(lambda x:-int(x), input().split()))
heapify(a)
for _ in range(m):
    x = heappop(a)
    x /= 2
    heappush(a, x)
print(-sum(map(lambda x : int(x), a)))