import heapq
import math

NN = 2020202
MOD = 10**9+7
INF = float("inf")

x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

que = [(-(A[0]+B[0]+C[0]), 0, 0, 0)]
seen = set([(0, 0, 0)])

for i in range(k):
    v, ai, bi, ci = heapq.heappop(que)
    print(-v)
    if ai < len(A)-1 and (ai+1, bi, ci) not in seen:
        seen.add((ai+1, bi, ci))
        heapq.heappush(que, (-(A[ai+1]+B[bi]+C[ci]), ai+1, bi, ci))
    if bi < len(B)-1 and (ai, bi+1, ci) not in seen:
        seen.add((ai, bi+1, ci))
        heapq.heappush(que, (-(A[ai]+B[bi+1]+C[ci]), ai, bi+1, ci))
    if ci < len(C)-1 and (ai, bi, ci+1) not in seen:
        seen.add((ai, bi, ci+1))
        heapq.heappush(que, (-(A[ai]+B[bi]+C[ci+1]), ai, bi, ci+1))

