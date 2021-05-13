from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
A = list(map(int, input().split()))

A = list(map(lambda x: x * (-1), A))

heapify(A)
for i in range(m):
    x = heappop(A)
    x = (x + 1) // 2
    heappush(A, x)

print(-1 * sum(A))
