import heapq
import math
N, M = map(int, input().split())
A = list(map(int,input().split()))

A = list(map(lambda x: x*(-1), A))
heapq.heapify(A)

for i in range(M):
    a = heapq.heappop(A)
    a = math.ceil(a / 2)
    heapq.heappush(A, a)

A = list(A)
print(sum(A)* (-1))