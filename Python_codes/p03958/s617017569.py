import heapq
k, t = map(int, input().split())
a = list(map(int, input().split()))
a = [-i for i in a]
heapq.heapify(a)
while len(a) > 1:
    m = heapq.heappop(a)
    while m < 0 and len(a) > 0:
        n = heapq.heappop(a)
        if n <= m:
            heapq.heappush(a, n-m)
            m = 0
        else:
            m -= n
    if m < 0:
        heapq.heappush(a, m)
res = heapq.heappop(a)

print(max(-res-1, 0))

