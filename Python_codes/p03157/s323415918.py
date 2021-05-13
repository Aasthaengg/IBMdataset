h,w = map(int, input().split())
m = [input() for _ in range(h)]
seen = [[0]*w for _ in range(h)]
dxy =[(1,0),(0,1),(-1,0),(0,-1)]
cnt = 0
for i in range(h):
  for j in range(w):
    if not seen[i][j]:
      bcnt,wcnt = 0,0
      q = [(i,j)]
      while q:
        y,x = q.pop()
        if seen[y][x]:
          continue
        if m[y][x] == "#":
          bcnt += 1
        else:
          wcnt += 1
        seen[y][x] = 1
        for dx,dy in dxy:
          if 0<=x+dx<w and 0<=y+dy<h and not seen[y+dy][x+dx] and m[y+dy][x+dx] != m[y][x]:
            q.append((y+dy,x+dx))
      cnt += bcnt*wcnt
print(cnt)