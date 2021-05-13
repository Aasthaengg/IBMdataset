import heapq
N, M = map(int, input().split())
A = [-int(i) for i in input().split()]
heapq.heapify(A)
for i in range(M):
    max_ = heapq.heappop(A)
    max_ = -max_//2
    heapq.heappush(A, -max_)
print(-sum(A))