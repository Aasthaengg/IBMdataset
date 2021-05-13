import heapq

n, m = map(int, input().split())
A = list(map(lambda x: int(x)*(-1), input().split()))

heapq.heapify(A)
for i in range(m):
    tmp = heapq.heappop(A)*(-1)
    heapq.heappush(A, (-1)*(tmp//2))
print(sum(A)*(-1))
