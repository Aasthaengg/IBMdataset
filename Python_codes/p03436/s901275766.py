from collections import deque
inf = 1000000000
h, w = map(int, input().split())
root = [[-1]*w for i in range(h)]
root[0][0] = 1
s = [[] for i in range(h)]

cnt = 0
for i in range(h):
    s[i] = input()
    for j in range(w):
        if s[i][j] == '#': cnt+=1
dw = [-1, 0, 1, 0]
dh = [0, 1, 0, -1]
que = deque()
que.append([0, 0])
while len(que)>0:
    x, y = que.popleft()
    for dx, dy in zip(dw, dh):
        nx, ny = x+dx, y+dy
        if 0<=nx<w and 0<=ny<h and root[ny][nx]==-1 and s[ny][nx]=='.':
                que.append([nx, ny])
                root[ny][nx] = root[y][x] + 1
if root[h-1][w-1]<0:
    print(-1)
else:
    print(h*w - cnt - root[h-1][w-1])