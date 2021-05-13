import heapq

n = int(input())
a = list(map(int, input().split()))
ans = 0

heapq.heapify(a)
b = list(map(lambda x: x * (-1), a))
heapq.heapify(b)
ans -= heapq.heappop(b)

for i in range(n//2-1):
    ans -= 2 * heapq.heappop(b)
if n % 2 == 1:
    ans -= heapq.heappop(b)
print(ans)
