import heapq

N, M = [int(x) for x in input().split()]
A = list([int(x) * - 1 for x in input().split()])
heapq.heapify(A)

for _ in range(M):
    target = heapq.heappop(A) * -1
    heapq.heappush(A, (target // 2) * -1)

print(sum(A) * -1)
