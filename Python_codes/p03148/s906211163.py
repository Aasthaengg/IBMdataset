import heapq

n, k = map(int, input().split())
a = [0] * (n + 1)
typecnt = 0
h = []
heapq.heapify(h)
for _ in range(n):
    t, d = map(int, input().split())
    if a[t] == 0:
        typecnt += 1
        a[t] = 1
    heapq.heappush(h, [-d, t])
ans = 0
mintype = 0
m = []
heapq.heapify(m)
for _ in range(k):
    d, t = heapq.heappop(h)
    if a[t] == 1:
        mintype += 1
        a[t] = 0
    else:
        heapq.heappush(m, -d)
    ans -= d
cnt = ans
ans += mintype * mintype
for j in range(mintype, typecnt):
    if not m:
        break
    bonus = (j + 1) * (j + 1)
    while h:
        d, t = heapq.heappop(h)
        if not m:
            break
        if a[t] == 1:
            a[t] = 0
            l = heapq.heappop(m)
            cnt -= (d + l)
            ans = max(ans, cnt + bonus)
            break
print(ans)