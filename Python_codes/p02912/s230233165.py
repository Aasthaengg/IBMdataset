import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = (-1)*A[i]

heapq.heapify(A)

for i in range(M):
    a = heapq.heappop(A)
    heapq.heappush(A, int(a/2))

print(abs(sum(A)))