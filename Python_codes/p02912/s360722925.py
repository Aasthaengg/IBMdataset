import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))

heapq.heapify(A)

for _ in range(M):
  Max = heapq.heappop(A) * -1
  heapq.heappush(A, Max//2 * -1)
  
ans = 0
for i in range(N):
  ans += -1 * A[i]
  
print(ans)