n, h, w = map(int, input().split())
sizes = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for size in sizes:
    if size[0] >= h and size[1] >= w:
        ans += 1
print(ans)
