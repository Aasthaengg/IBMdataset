from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sushi = [None] * N
for i in range(N):
    t, d = map(int, input().split())
    sushi[i] = (d, t-1)
sushi.sort(reverse=True)

types = set()
cand = []
s = x = 0

for d, t in sushi[:K]:
    if t in types:
        heappush(cand, d)
    else:
        types.add(t)
        x += 1
    s += d

ans = s + x*x
for d, t in sushi[K:]:
    if t in types:
        continue
    if not cand:
        break
    dr = heappop(cand)
    s += d - dr
    types.add(t)
    x += 1
    ans = max(ans, s + x*x)
print(ans)

