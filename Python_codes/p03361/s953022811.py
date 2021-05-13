H, W = map(int, input().split())
s = list(list(input()) for _ in range(H))
ans = True
d = [(0,1),(0,-1),(1,0),(-1,0)]
for y in range(H):
    for x in range(W):
        if s[y][x] == "#":
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if ny<0 or H<=ny or nx<0 or W<=nx:
                    continue
                if s[ny][nx]=="#":
                    break
            else:
                ans = False
print("Yes" if ans else "No")