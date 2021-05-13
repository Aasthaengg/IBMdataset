import math
import heapq
n, m = map(int, input().split())
a = [int(i) * (-1) for i in input().split()]
heapq.heapify(a)
i = 0
while i < m:
    max_a = - heapq.heappop(a)
    max_a /= 2
    heapq.heappush(a, -max_a)
    i += 1
total = 0
for k in a:
    total += math.floor(-k)
print(total)