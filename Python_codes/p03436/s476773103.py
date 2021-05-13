from collections import deque
H, W = map(int, input().split())
S = list(input() for _ in range(H))
dist = [[-1]*W for _ in range(H)]
dist[0][0] = 1

d = deque([[0, 0, 1]])
while d:
    x, y, c = deque.popleft(d)
    if x > 0:
        if dist[x-1][y] == -1 and S[x-1][y] == ".":
            dist[x-1][y] = c+1
            deque.append(d, [x-1, y, c+1])
    if y > 0:
        if dist[x][y-1] == -1 and S[x][y-1] == ".":
            dist[x][y-1] = c+1
            deque.append(d, [x, y-1, c+1])
    if x < H-1:
        if dist[x+1][y] == -1 and S[x+1][y] == ".":
            dist[x+1][y] = c+1
            deque.append(d, [x+1, y, c+1])
    if y < W-1:
        if dist[x][y+1] == -1 and S[x][y+1] == ".":
            dist[x][y+1] = c+1
            deque.append(d, [x, y+1, c+1])

road = 0
for ss in S:
    for s in ss:
        if s == ".":
            road += 1
if dist[H-1][W-1] == -1:
    print(-1)
else:
    print(road-dist[H-1][W-1])
