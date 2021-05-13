h, w = map(int, input().split())
M = [str(input()) for _ in range(h)]

cnt = 0
for i in range(h):
    cnt += M[i].count('.')

M = ['#'*w] + M + ['#'*w]
M = ['#'+c+'#' for c in M]

sy, sx = 1, 1

from collections import deque
stack = deque()
stack.append((sy, sx))
visit = [[-1]*(w+2) for _ in range(h+2)]
visit[sy][sx] = 0

while stack:
    y, x = stack.popleft()
    if y == h and x == w:
        break
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        new_y, new_x = y+dy, x+dx
        if visit[new_y][new_x] == -1 and M[new_y][new_x] != '#':
            visit[new_y][new_x] = visit[y][x]+1
            stack.append((new_y, new_x))
else:
    print(-1)
    exit()

print(cnt-(visit[h][w]+1))
