import heapq

n, m = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapq.heapify(A)
for _ in range(m):
    max_price = -heapq.heappop(A) // 2
    heapq.heappush(A, -max_price)
total = -sum(A)
print(total)
