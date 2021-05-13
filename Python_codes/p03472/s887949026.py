import heapq

n, h = map(int, input().split())

hq = []

for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(hq, [-a, float("inf")])
    heapq.heappush(hq, [-b, 1])

ans = 0
while h > 0:
    damage, cnt = heapq.heappop(hq)
    damage = -damage

    if cnt == float("inf"):
        ans += (h + damage - 1) // damage
        h = 0
        heapq.heappush(hq, [-damage, float("inf")])
    else:
        ans += 1
        h -= damage

print(ans)
