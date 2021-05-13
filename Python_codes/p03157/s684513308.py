dy = (-1,0,1,0)
dx = (0,1,0,-1)

h,w = map(int,input().split())
grid = [input() for _ in range(h)]

ans = 0
dist = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if dist[i][j] < 0:
            odd = 0
            even = 1
            dist[i][j] = 0
            stack = [(i,j)]
            while stack:
                a,b = stack.pop()
                if grid[a][b] == '#':
                    for k in range(4):
                        y = a + dy[k]
                        x = b + dx[k]
                        if y < 0 or y >= h:
                            continue
                        if x < 0 or x >= w:
                            continue
                        if grid[y][x] == '.' and dist[y][x] < 0:
                            if dist[a][b] == 0:
                                dist[y][x] = 1
                                odd += 1
                            else:
                                dist[y][x] = 0
                                even += 1
                            stack.append((y,x))
                else:
                    for k in range(4):
                        y = a + dy[k]
                        x = b + dx[k]
                        if y < 0 or y >= h:
                            continue
                        if x < 0 or x >= w:
                            continue
                        if grid[y][x] == '#' and dist[y][x] < 0:
                            if dist[a][b] == 0:
                                dist[y][x] = 1
                                odd += 1
                            else:
                                dist[y][x] = 0
                                even += 1
                            stack.append((y,x))    
            ans += even * odd
print(ans)