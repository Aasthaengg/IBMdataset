from collections import deque


def resolve():
    H, W = map(int, input().split())
    maze = []
    cnt = 0
    for i in range(H):
        maze.append(list(input()))
        cnt += maze[-1].count('#')
    
    d = [[float('inf')] * W for _ in range(H)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    q = deque([(0, 0)])
    d[0][0] = 0
    goal = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (1
                    and 0 <= ny < H
                    and 0 <= nx < W
                    and maze[ny][nx] != '#'
                    and d[ny][nx] == float('inf')):
                q.append((ny, nx))
                d[ny][nx] = d[y][x] + 1
        if d[H - 1][W - 1] != float('inf'):
            goal = d[H - 1][W - 1] + 1
            break
    if goal:
        print(H * W - goal - cnt)
    else:
        print(-1)

if __name__ == "__main__":
    resolve()
