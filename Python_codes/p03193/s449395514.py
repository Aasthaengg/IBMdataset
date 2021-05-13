n, h, w = map(int, input().split())
g = []
for i in range(n):
    a, b = map(int, input().split())
    g.append([a, b])
ans = 0
for ai, bi in g:
    if ai >= h and bi >= w:
        ans += 1

print(ans)