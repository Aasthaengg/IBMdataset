from collections import defaultdict as dd
from heapq import heappop, heappush

N, K = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x:-x[1])
used = set()
q2, q3 = [], []

score, kind = 0, 0

for t, d in l[:K]:
    score += d
    if t in used:
        heappush(q3, d)
    else:
        used.add(t)
        kind += 1

ans = score + kind*kind

q1 = dd(list)
for t, d in l[K:]:
    if not t in used:
        heappush(q1[t], -d)
for t in q1.keys():
    d = heappop(q1[t])
    heappush(q2, d)

while q2 and q3:
    d1 = heappop(q2)
    d1 = -d1

    d2 = heappop(q3)
    score -= d2
    score += d1
    kind += 1
    ans = max(ans, score + kind*kind)

print(ans)