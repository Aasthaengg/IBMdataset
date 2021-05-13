from collections import deque
h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]
dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

sh, sw, gh, gw = 0, 0, h - 1, w - 1
d = [[float("inf")] * w for _ in range(h)]

que = deque([])
que.append((sh, sw))
d[sh][sw] = 0


def bfs():
    while que:
        p = que.popleft()
        if p[0] == gh and p[1] == gw:
            break
        for i in range(4):
            nh = p[0] + dh[i]
            nw = p[1] + dw[i]
            if 0 <= nh < h and 0 <= nw < w and maze[nh][nw] != "#" and d[nh][nw] == float("inf"):
                que.append((nh, nw))
                d[nh][nw] = d[p[0]][p[1]] + 1
    return d[gh][gw]

##最短距離を格納
bfs = bfs()
cnt = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            cnt += 1
if bfs == float("inf"):
    print(-1)
else:
    print(cnt - (bfs + 1))
