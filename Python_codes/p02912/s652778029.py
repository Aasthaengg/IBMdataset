import heapq

n, m = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))

heapq.heapify(A)
for i in range(m):
    item = heapq.heappop(A)
    heapq.heappush(A, (-1) * (-item // 2))

print(-sum(A))