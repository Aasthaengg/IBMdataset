n, m= map(int, input().split())
h = list(map(int, input().split()))

e = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    e[a-1].append(b-1)
    e[b-1].append(a-1)

ans = 0
for j in range(n):
    if not e[j]:
        ans += 1
        continue
    hs = [h[k] for k in e[j]]
    if h[j] > max(hs):
        ans += 1
print(ans)


