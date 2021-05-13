import heapq

n, m = map(int, input().split())
alst = list(map(int, input().split()))
heap = [-1 * num for num in alst]
ans = sum(alst)
heapq.heapify(heap)

num = heapq.heappop(heap)
for _ in range(m):
    num *= -1
    tmp = num // 2
    ans -= num - tmp
    tmp *= -1
    num = heapq.heappushpop(heap, tmp)
print(ans)
