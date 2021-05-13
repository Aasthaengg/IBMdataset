import heapq
n, k = map(int, input().split())
hq = []
total = 0
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(hq, (-a, b))
    total += b

while total >= k:
    a, b = heapq.heappop(hq)
    total -= b

print(abs(a))