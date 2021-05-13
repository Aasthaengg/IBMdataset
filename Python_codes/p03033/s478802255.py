from bisect import bisect_left
import heapq
n, q = map(int, input().split())
stx = [tuple(map(int, input().split())) for _ in range(n)]
d = [int(input()) for _ in range(q)]

events = []
for s, t, x in stx:
    events.append((s-x, 1, x))
    events.append((t-x, -1, x))
events.sort(key=lambda x: x[0])

hp = []
st = set()
res = [-1] * q
now = 0
for t, b, x in events:
    while now < q and d[now] < t:
        if len(st) > 0:
            while hp[0] not in st:
                heapq.heappop(hp)
            res[now] = hp[0]
        now += 1
    if b == 1:
        heapq.heappush(hp, x)
        st.add(x)
    else:
        st.discard(x)
print(*res)