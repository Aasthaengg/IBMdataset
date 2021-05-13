from heapq import heappushpop, heapify

N, M = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

heap = [-a for a in A]
heapify(heap)

for _ in range(M):
    heappushpop(heap, (-1 * heap[0] // 2) * -1)

print(-1 * sum(heap))
