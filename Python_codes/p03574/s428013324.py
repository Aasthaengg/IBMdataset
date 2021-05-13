h,w = map(int, input().split())
grid = [list(input()) for _ in range(h)]


dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            cnt = 0
            for k in range(8):
                nx = j + dx[k]
                ny = i + dy[k]            
                if (nx < 0) or (w-1 < nx) or (ny < 0) or (h-1 < ny):
                    continue
                elif grid[ny][nx] == "#":
                    cnt += 1
                else:
                    pass
            grid[i][j] = cnt
for i in range(h):
  ans = ''.join(map(str,grid[i]))
  print(ans)