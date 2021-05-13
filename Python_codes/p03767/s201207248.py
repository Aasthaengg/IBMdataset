import heapq

N = int(input())
a = list(map(int, input().split()))

ans = 0
b = list(map(lambda x: x * (-1), a))
heapq.heapify(b)
for _ in range(N):
    heapq.heappop(b)
    ans -= heapq.heappop(b)
print(ans)