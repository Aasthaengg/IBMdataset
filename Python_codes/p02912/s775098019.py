import heapq

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
A = list(map(lambda x: x * (-1), A))
heapq.heapify(A)

for x in range(M):
    maxA = heapq.heappop(A)
    heapq.heappush(A, -1 * ((-1 * maxA) // 2))
A = list(map(lambda x: x * (-1), A))

print(sum(A))
