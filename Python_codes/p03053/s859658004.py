from collections import deque

h, w = map(int, input().split())

as_ = []
for i in range(h):
    a = [s for s in input().split()]
    for a_ in a:
        as_.append(a_)

ds = [[None]*w for _ in range(h)]
# ds = [[None]*w]*h ←これだとうまくいかないので注意

starts = deque()
for i, a in enumerate(as_):
    for j, a_ in enumerate(a):
        if a_ == "#":
            ds[i][j] = 0
            starts.append((i,j))
def bfs(starts, ds):
    d = 0
    while starts:
        i, j = starts.popleft()
        d = ds[i][j]
        for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni = i + my
            nj = j + mx
            if 0 <= ni < h and 0 <= nj < w:
                if ds[ni][nj] == None:
                    ds[ni][nj] = d + 1
                    starts.append((ni, nj))
    return d
d = bfs(starts, ds)
print(d)