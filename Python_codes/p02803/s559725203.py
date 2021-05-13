H,W = map(int,input().split())
maze = []
for i in range(H):
    maze.append(list(input()))

queue = []
visited = []
visited = [[0 for _ in range(W)] for _ in range(H)]
ans = 0

for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            queue.append([i,j])
            visited[i][j] = 1

            while len(queue) > 0:
                now_y, now_x = map(int,queue.pop(0))
                for next_x, next_y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    y = now_y + next_y
                    x = now_x + next_x
                    if 0 <= y < H and 0 <= x < W:
                        if maze[y][x] != '#' and visited[y][x] == 0:
                            visited[y][x] = visited[now_y][now_x] + 1
                            queue.append([y,x])

        for l in range(H):
            for m in range(W):
                ans = max(ans,visited[l][m])

        queue = []
        visited = [[0 for _ in range(W)] for _ in range(H)]



print(ans-1)
