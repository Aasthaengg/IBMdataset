from queue import Queue
H, W = map(int, input().split())
S=[input() for _ in range(H)]

def bfs(sy, sx):
    mx=0
    q=Queue()
    dist=[[-1]*W for _ in range(H)]
    q.put((sy,sx))
    dist[sy][sx]=0
    while not q.empty():
        y, x=q.get()
        y_nxt=[y+1, y-1, y, y]
        x_nxt=[x, x, x+1, x-1]
        for Y,X in zip(y_nxt, x_nxt):
            if not (0 <= Y < H) or not (0 <= X < W) or S[Y][X]=="#":
                continue
            if dist[Y][X]==-1:
                dist[Y][X]=dist[y][x]+1
                q.put((Y, X))
                mx=max(mx, dist[Y][X])
    return mx

mx=0
for y in range(H):
    for x in range(W):
        if S[y][x]=="#":
            continue
        else:
            mx=max(bfs(y,x),mx)

print(mx)