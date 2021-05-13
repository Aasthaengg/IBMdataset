from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [-i for i in a]
heapify(a)

for i in range(m):
    x = heappop(a)
    heappush(a, int(x/2))

ans = 0
for i in range(n):
    ans += -a[i]
print(ans)