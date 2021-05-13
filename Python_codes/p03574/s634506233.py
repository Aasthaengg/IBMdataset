h, w = map(int, input().split()) #hが行(x)、wが列(y)
maze = [input() for i in range(h)]
bomb = [[0] * w for _ in range(h)]

for x in range(h):
    for y in range(w):
        if maze[x][y] == "#":
            bomb[x][y] = "#"
            continue

        for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            nx = x + dx
            ny = y + dy 
            if not 0 <= nx < h or not 0 <= ny < w:
                continue
            if maze[nx][ny] == "#":
                bomb[x][y] += 1
               



for i in range(h):
    ans = ""
    for j in range(w):     
        ans +=str( bomb[i][j])
    print(ans)
        
       
