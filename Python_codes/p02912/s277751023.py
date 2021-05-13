import heapq
N, M = map(int, input().split())
*A, = map(int, input().split())

A = list(map(lambda x: x*(-1), A))  # 各要素を-1倍
heapq.heapify(A)

while M>0:
    a = heapq.heappop(A)*(-1)
    heapq.heappush(A, -int(a/2))
    M -= 1

print(-sum(A))