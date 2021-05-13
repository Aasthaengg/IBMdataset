from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

cnt_white = 0
for row in s:
    cnt_white += row.count('.')

d = deque([[0, 0]])
dist = [[-1] * w for _ in range(h)]
dist[0][0] = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
goal_flag = False
while d:
    x, y = d.popleft()
    if x == h - 1 and y == w - 1:
        goal_flag = True
        break
    for i in range(4):
        pos_x, pos_y = x + dx[i], y + dy[i]
        if 0 <= pos_x < h and 0 <= pos_y < w and s[pos_x][pos_y] == '.' and dist[pos_x][pos_y] == -1:
            d.append([pos_x, pos_y])
            dist[pos_x][pos_y] = dist[x][y] + 1

if goal_flag:
    print(cnt_white - dist[h-1][w-1] - 1)
else:
    print(-1)