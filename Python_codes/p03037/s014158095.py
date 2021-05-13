n, m = map(int, input().split())
l, r = [], []

for _ in range(m):
    s, t = map(int, input().split())
    l.append(int(s))
    r.append(int(t))

ans = min(r) - max(l) + 1 if min(r) >= max(l) else 0
print(ans)
