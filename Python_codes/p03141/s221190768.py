import heapq

n = int(input())
happy = []
ans = 0
for i in range(n):
    a, b = tuple(map(int, input().split()))
    heapq.heappush(happy, - (a + b))
    ans += a
while len(happy) != 0:
    heapq.heappop(happy)
    if len(happy) != 0:
        h = heapq.heappop(happy)
        ans += h
    else:
        break
print(ans)
