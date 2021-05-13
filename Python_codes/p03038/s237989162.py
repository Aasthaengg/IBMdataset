n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
bc = sorted([list(map(int, input().split())) for i in range(m)], key=lambda x:x[1], reverse=True)
ans = 0
x, y = 0, 0
for i in range(n):
    if y == m or a[x] > bc[y][1]:
        ans += a[x]
        x += 1
    else:
        ans += bc[y][1]
        bc[y][0] -= 1
        if bc[y][0] == 0:
            y += 1
print(ans)