
from heapq import heappop, heappush

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

pq = []
heappush(pq, (-A[0] - B[0] - C[0], 0, 0, 0))
appeared = set((0, 0, 0))

for _ in range(K):
    # Pop maximum value
    val, i, j, k = heappop(pq)
    print(-val)

    # Add next value
    if i + 1 < X and (i + 1, j, k) not in appeared:
        heappush(pq, (-A[i + 1] - B[j] - C[k], i + 1, j, k))
        appeared.add((i + 1, j, k))

    if j + 1 < Y and (i, j + 1, k) not in appeared:
        heappush(pq, (-A[i] - B[j + 1] - C[k], i, j + 1, k))
        appeared.add((i, j + 1, k))

    if k + 1 < Z and (i, j, k + 1) not in appeared:
        heappush(pq, (-A[i] - B[j] - C[k + 1], i, j, k + 1))
        appeared.add((i, j, k + 1))
