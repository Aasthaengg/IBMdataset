from collections import deque

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

root = [[float("inf") for _ in range(w)] for _ in range(h)]
root[0][0] = 1
D = deque([[0, 0]])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while D:
    p = D.popleft()

    if p == [h-1, w-1]:
        break

    for i in range(4):
        x = p[0]+dx[i]
        y = p[1]+dy[i]
        if 0<=x<=h-1 and 0<=y<=w-1 and root[x][y]==float("inf") and maze[x][y]==".":
            root[x][y] = root[p[0]][p[1]] + 1
            D.append([x, y])

white = 0
for i in range(h):
    for j in range(w):
        if maze[i][j]==".":
            white += 1

if root[h-1][w-1] ==float("inf"):
    print(-1)
else:
    print(white - root[h-1][w-1])