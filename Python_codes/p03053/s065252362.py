h, w = map(int, input().split())
a = [list(input()) for i in range(h)]
que = []
v = [[True] * (w + 2)]
v += [[True] + [j == "#" for j in a[i]] + [True] for i in range(h)]
v.append([True] * (w + 2))
m = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if v[i][j]:
            que.append((i, j))
ans = 0
while que:
    p = []
    ans += 1
    for x, y in que:
        if not v[x - 1][y]:
            v[x - 1][y] = True
            p.append((x - 1, y))
        if not v[x + 1][y]:
            v[x + 1][y] = True
            p.append((x + 1, y))
        if not v[x][y - 1]:
            v[x][y - 1] = True
            p.append((x, y - 1))
        if not v[x][y + 1]:
            v[x][y + 1] = True
            p.append((x, y + 1))
    que = p
print(ans - 1)