h, w = map(int, input().split())
maze = []
for _ in range(h):
    maze.append(list(input()))
import collections
black = collections.deque([])
cnt = 0
for hh in range(h):
    for ww in range(w):
        if maze[hh][ww] == "#":
            cnt += 1
            black.append([hh, ww, 0])
dh = [ 0, -1, 1, 0]
dw = [ -1, 0, 0, 1]
res = 0
allcount = h*w
res = 0
while cnt < allcount:
    #print("black:", black)
    bh, bw , bturn= black.popleft()
    #print("pop", bh, bw, bturn)
    for di in range(len(dh)):
        nh = bh + dh[di]
        nw = bw + dw[di]
        if nh < 0 or nh > (h-1) or nw < 0 or nw > (w-1):
            continue
        if maze[nh][nw] == "#":
            continue
        black.append([nh, nw, bturn+1])
        #print(nh, nw)
        maze[nh][nw] = "#"
        res = max(res, bturn+1)
        cnt += 1
print(res)

