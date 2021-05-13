H, W = map(int,input().split())

S = [input() for _ in range(H)]

a = [[0] * W for _ in range(H)] # 右
b = [[0] * W for _ in range(H)] # 左
c = [[0] * H for _ in range(W)] # 上
d = [[0] * H for _ in range(W)] # 下

for x in range(H):
    for y in range(W):
        if S[x][y] == '#':
            a[x][y] = -1
        elif y > 0:
            a[x][y] = a[x][y-1] + 1
            
for x in range(H):
    for y in range(W-1,-1,-1):
        if S[x][y] == '#':
            b[x][y] = -1
        elif y < W-1:
            b[x][y] = b[x][y+1] + 1

for y in range(W):
    for x in range(H):
        if S[x][y] == '#':
            c[y][x] = -1
        elif x > 0:
            c[y][x] = c[y][x-1] + 1

for y in range(W):
    for x in range(H-1,-1,-1):
        if S[x][y] == '#':
            d[y][x] = -1
        elif x < H-1:
            d[y][x] = d[y][x+1] + 1

ans = 0

for x in range(H):
    for y in range(W):
        if S[x][y] != '#':
            ans = max(ans,a[x][y]+b[x][y]+c[y][x]+d[y][x]+1)

print(ans)