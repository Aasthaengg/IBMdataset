from queue import Queue
import copy

h, w = map(int, input().split())

f = [["#"] * (w + 2)] + \
    [list("#" + input() + "#") for i in range(h)] + \
    [["#"] * (w + 2)]
dxy = [(0,1), (0,-1), (1,0), (-1,0)]

d = [[-1]*(w+2) for i in range(h+2)]
for iy in range(h+2):
    for ix in range(w+2):
        if f[iy][ix] == '#':
            d[iy][ix] = 1000

ans = 0
for sy in range(h+2):
    for sx in range(w+2):
        if f[sy][sx] == '#':
            continue
        dist = copy.deepcopy(d)
        cnt = 0
        cnt_max = 0
        q = Queue()
        q.put([sy, sx])
        dist[sy][sx] = 0
        while q.qsize():
            y, x = q.get()
            cnt = dist[y][x]
            
            # print(sx, sy, x, y)
            cnt_max = max(cnt_max, cnt)
            for dy, dx in dxy:
                ny, nx = y + dy, x + dx
                if dist[ny][nx] == 1000:
                    continue
                if dist[ny][nx] == -1:
                    q.put([ny, nx])
                    dist[ny][nx] = cnt + 1
        # print(sx, sy, x, y, cnt)
        ans = max(ans, cnt_max)
print(ans)