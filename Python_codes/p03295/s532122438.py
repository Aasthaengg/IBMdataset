n, m = map(int, input().split())
L = []
for _ in range(m):
    a, b = map(int, input().split())
    L.append((a, b))
L = sorted(L, key=lambda x: x[1])
ans = 0
r = -float('inf')
for i in L:
    if i[0] >= r:
        ans += 1
        r = i[1]
print(ans)
