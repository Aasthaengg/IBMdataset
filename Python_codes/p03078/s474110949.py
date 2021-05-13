from heapq import heappop, heappush, heapify

X, Y, Z, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

heap = list()
used = set()
res = list()

heappush(heap, (-(A[0] + B[0] + C[0]), 0, 0, 0))
used.add((0, 0, 0))

for _ in range(K):
    v, i, j, k = heappop(heap)
    res.append(-v)
    if i + 1 < X and (i + 1, j, k) not in used:
        used.add((i + 1, j, k))
        heappush(heap, (-(A[i + 1] + B[j] + C[k]), i + 1, j, k))
    if j + 1 < Y and (i, j + 1, k) not in used:
        used.add((i, j + 1, k))
        heappush(heap, (-(A[i] + B[j + 1] + C[k]), i, j + 1, k))
    if k + 1 < Z and (i, j, k + 1) not in used:
        used.add((i, j, k + 1))
        heappush(heap, (-(A[i] + B[j] + C[k + 1]), i, j, k + 1))
        
print('\n'.join(map(str, res)))