
h,w = map(int,input().split())

def isvalid(r,c):
    return 0 <= r < h and 0 <= c < w

g = [input() for _ in range(h)]
d = [1,0]
queue = [(0,0)]
dist = [[1000000]* w for _ in range(h)]
dist[0][0] = 0
if g[0][0] == '#':
    dist[0][0] = 1
while len(queue) > 0:
    next_queue = []
    for r,c in queue:
        for i in range(2):
            cos = dist[r][c]
            nr = r + d[i]
            nc = c + d[1^i]
            if not isvalid(nr,nc):
                continue
            if  g[r][c] != g[nr][nc]:
                cos += 1
            if cos < dist[nr][nc]:
                dist[nr][nc] = cos
                next_queue.append((nr,nc))
    queue = next_queue
print((dist[h-1][w-1] + 1)//2)