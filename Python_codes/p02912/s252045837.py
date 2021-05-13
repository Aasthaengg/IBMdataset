from heapq import *
N, M = map(int, input().split())
A = []
for a in map(int, input().split()):
    heappush(A, -a)
for _ in range(M):
    x = -heappop(A)
    x //= 2
    heappush(A, -x)
print(-sum(A))