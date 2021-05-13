from collections import defaultdict
from heapq import heappush,heappop

# map(int, input().split())
N, Q = map(int, input().split())
events = []
for i in range(N):
    s, t, x = map(int, input().split())
    events.append((s - x, 0, x))
    events.append((t - x, 1, x))

for i in range(Q):
    d = int(input())
    events.append((d, 2, i))

events = sorted(events)
INF = 10**13
q = [INF]
cnt = defaultdict(int)
ans = [INF]*Q
for a,b,c in events:
    if b == 0:
        heappush(q,c)
        cnt[c] += 1
    elif b==1:
        cnt[c] -= 1
    else:
        while len(q) > 1 and cnt[q[0]] == 0:
            heappop(q)
        if q[0] == INF:
            ans[c] = -1
        else:
            ans[c] = q[0]
for a in ans:
    print(a)
