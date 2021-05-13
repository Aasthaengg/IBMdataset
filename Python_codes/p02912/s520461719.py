n, m = map(int, input().split())

A = list(map(int, input().split()))

import heapq

A = list(map(lambda x: x*(-1), A))

heapq.heapify(A)

for i in range(m):
    val = heapq.heappop(A)
    val = (-1 * val)//2 * (-1)
    heapq.heappush(A, val)

print(sum(list(map(lambda x: x*(-1), A))))