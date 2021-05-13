import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = -A[i]
heapq.heapify(A)

for i in range(M):
    a = heapq.heappop(A)*(-1)
    if a ==0:#最大値が0になったら終了
        break
    a//=2
    heapq.heappush(A, -a)
print(-sum(A))