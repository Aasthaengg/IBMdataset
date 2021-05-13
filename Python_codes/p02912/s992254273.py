from heapq import heapify,heappush,heappop
N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapify(A)
for i in range(M):
  tmp = heappop(A)
  heappush(A,-((-tmp)//2))
A = list(A)

print(-sum(A))
