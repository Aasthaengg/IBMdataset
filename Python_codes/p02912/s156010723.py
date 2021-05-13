import heapq
import math
from heapq import heappop
n,m = map(int,input().split())
A = list(map(lambda x:-int(x),input().split()))
heapq.heapify(A)

for i in range(m):
    x = heapq.heappop(A)
    heapq.heappush(A,-(-x//2))

print(-sum(A))