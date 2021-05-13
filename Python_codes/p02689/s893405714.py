n, m = map(int, input().split())
h = list(map(int, input().split()))
eg = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    eg[a].append(b)
    eg[b].append(a)

ans = 0
for i in range(1, n + 1):
    high = True
    for to in eg[i]:
        if h[i - 1] <= h[to - 1]:
            high = False
    if high:
        ans += 1
print(ans)
