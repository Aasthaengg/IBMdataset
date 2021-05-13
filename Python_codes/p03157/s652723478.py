h,w = map(int,input().split())
s = [str(input()) for i in range(h)]

dxdy = {(-1, 0), (1, 0), (0, -1), (0, 1)}

ch = [[0] * w for i in range(h)]

ans = 0

for i in range(h):
    for j in range(w):
        if ch[i][j] == 0:
            black,white = 0,0
            q = [(i,j)]
            while q:
                y,x = q.pop()
                if ch[y][x] == 0:
                    if s[y][x] == "#":black += 1
                    else:white += 1
                    ch[y][x] = 1
                    for dx,dy in dxdy:
                        if 0 <= x + dx < w and 0 <= y + dy < h and ch[y+dy][x+dx] == 0 and s[y+dy][x+dx] != s[y][x]:
                            q.append((y+dy,x+dx))
            ans += black * white

print(ans)