# coding: utf-8
import sys
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 虫の目、一個ずつheapへ
X, Y, Z, K = lr()
A = lr(); A.sort(reverse=True)
B = lr(); B.sort(reverse=True)
C = lr(); C.sort(reverse=True)

ma = A[0] + B[0] + C[0]
heap = [(-ma, (0, 0, 0))]
used = set()
for _ in range(K):
    result, place = heappop(heap)
    print(-result)
    i, j, k = place
    p = (i+1, j, k)
    if i + 1 < len(A) and p not in used:
        val = A[i+1] + B[j] + C[k]
        used.add(p)
        heappush(heap, (-val, p))
    p = (i, j+1, k)
    if j + 1 < len(B) and p not in used:
        val = A[i] + B[j+1] + C[k]
        used.add(p)
        heappush(heap, (-val, p))
    p = (i, j, k+1)
    if k + 1 < len(C) and p not in used:
        val = A[i] + B[j] + C[k+1]
        used.add(p)
        heappush(heap, (-val, p))

# 26
