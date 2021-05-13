import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

X, Y, Z, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

cakes = []

heappush(cakes, (-(A[0]+B[0]+C[0]),0, 0, 0))

visited = set((A[0], B[0], C[0]))

for i in range(K):
    v, a, b, c = heappop(cakes)
    print(-v)

    if a+1 <= len(A) - 1 and (a+1, b, c) not in visited:
        v = A[a+1] + B[b] + C[c]
        heappush(cakes, (-v, a+1, b, c))
        visited.add((a+1, b, c))
    if b+1 <= len(B) - 1 and (a, b+1, c) not in visited:
        v = A[a] + B[b+1] + C[c]
        heappush(cakes, (-v, a, b+1, c))
        visited.add((a, b+1, c))
    if c+1 <= len(C) - 1 and (a, b, c+1) not in visited:
        v = A[a] + B[b] + C[c+1]
        heappush(cakes, (-v, a, b, c+1))
        visited.add((a, b, c+1))