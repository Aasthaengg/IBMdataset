import heapq

k, t = map(int, input().split())
a = list(map(int, input().split()))

q = []
heapq.heapify(q)

for i in range(t):
    heapq.heappush(q, [a[i] * -1, i])

ans = 0
prev = -1

while len(q) > 0:
    num, idx = heapq.heappop(q)
    if idx == prev and len(q) > 0:
        num2, idx2 = heapq.heappop(q)
        heapq.heappush(q, [num, idx])
        num, idx = num2, idx2

    if idx == prev:
        ans += 1
    num *= -1
    num -= 1
    if num > 0:
        heapq.heappush(q, [num * -1, idx])
    prev = idx

print(ans)
