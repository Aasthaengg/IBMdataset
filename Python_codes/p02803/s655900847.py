# ABC151 D-Maze Master
import queue
H,W = map(int,input().split())
maze = [input() for _ in range(H)]
dydx = ((0,1),(0,-1),(1,0),(-1,0))

def reach(sy,sx):
    visited = [[0]*W for _ in range(H)]
    visited[sy][sx] = 1
    q = queue.Queue()
    q.put((sy,sx,0))
    while True:
        y,x,d = q.get()
        for dy,dx in dydx:
            if (0<=y+dy<H)&(0<=x+dx<W):
                if (maze[y+dy][x+dx] == '#') or (visited[y+dy][x+dx] == 1):
                    continue
                visited[y+dy][x+dx] = 1
                q.put((y+dy,x+dx,d+1))
        if q.empty():
            ans = d
            break
    return ans

d = -1
for sy in range(H):
    for sx in range(W):
        if maze[sy][sx] == '#':
            continue
        d = max(d,reach(sy,sx))
                
print(d)