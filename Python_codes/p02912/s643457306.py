import heapq
N, M = map(int, input().split())
heap = list(map(lambda x: -1*int(x), input().split()))
heapq.heapify(heap)

while M > 0:
    x = heapq.heappop(heap)
    heapq.heappush(heap, int(x/2))
    M -= 1
print(sum(heap)*(-1))