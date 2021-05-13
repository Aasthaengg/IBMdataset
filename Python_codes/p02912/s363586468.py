import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x * (-1), A))
heapq.heapify(A)
for i in range(M):
    b = heapq.heappop(A) * (-1)
    b = b // 2 * (-1)
    heapq.heappush(A, b)
print(sum(A) * -1)