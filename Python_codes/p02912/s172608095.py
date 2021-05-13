import heapq
import math
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x*(-1), a))
ticket_num = m
heapq.heapify(a)

if n > 1:
    for i in range(m):
        MAX = heapq.heappop(a)
        MAX = math.ceil(MAX / 2)
        heapq.heappush(a,MAX)
        
else:
    MAX = heapq.heappop(a)
    MAX = math.ceil(MAX / (2**m))
    heapq.heappush(a,MAX)

print(sum(a)*(-1))