def resolve():
    from collections import deque
    h, w = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    visited = [[-1]*w for _ in range(h)]
    nxt = [[0,0]]
    nxt = deque(nxt)
    visited[0][0] = 1
    while nxt:
        x, y = nxt.popleft()
        for i, j in ([1,0], [0,1], [-1,0], [0,-1]):
            nx = x+ i
            ny = y+j
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny]== -1 and maze[nx][ny] != "#":
                visited[nx][ny] = visited[x][y] + 1
                nxt.append([nx, ny])
    totalsharp = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] == "#":
                totalsharp += 1
    if visited[h-1][w-1] == -1:
        print(-1)
    else:
        print(h*w-totalsharp-visited[h-1][w-1])
resolve()