import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sushi = [None] * N
for i in range(N):
    t, d = map(int, input().split())
    sushi[i] = (d, t)
sushi.sort(reverse=True)

types = set()
cand = []
s = x = 0

for d, t in sushi[:K]:
    if t in types:
        cand.append(d)
    else:
        types.add(t)
        x += 1
    s += d
cand.sort(reverse=True)

ans = s + x*x
for d, t in sushi[K:]:
    if t in types:
        continue
    if not cand:
        break
    dr = cand.pop()
    s += d - dr
    types.add(t)
    x += 1
    ans = max(ans, s + x*x)
print(ans)