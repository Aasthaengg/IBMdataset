import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
  A[i] = -A[i]
heapq.heapify(A)
for _ in range(M):
  a = -heapq.heappop(A)
  a = (a//2) * -1
  heapq.heappush(A, a)
print(sum(A)*-1)