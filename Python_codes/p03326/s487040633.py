n, m = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(8):
    a = []
    for x, y, z in cakes:
        if i & 1 << 0: x *= -1
        if i & 1 << 1: y *= -1
        if i & 1 << 2: z *= -1
        a.append(x + y + z)
    a.sort(reverse=True)
    ans = max(ans, sum(a[:m]))

print(ans)
