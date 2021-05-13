import collections

h, w = list(map(int, input().split()))
smat = [input() for _ in range(h)]

def bfs(x0, y0):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    deq = collections.deque()
    deq.append((x0, y0, -1))

    mx = 0
    while len(deq) > 0:
        x, y, d = deq.popleft()
        nd = d + 1
        visited[x][y] = 1
        mx = max(mx, nd)

        for dx, dy in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < h) or not (0 <= ny < w):
                # bound check
                continue
            if smat[nx][ny] == '#':
                # cell attr check
                continue
            if visited[nx][ny] == 1:
                # already visited
                continue
            v = (nx, ny, nd)
            deq.append(v)
    
    return mx

if all(all(col == '.' for col in row) for row in smat):
    print((w - 1) + (h - 1))
else:
    mxall = 0
    for x0 in range(h):
        for y0 in range(w):
            if smat[x0][y0] == '.':
                mx = bfs(x0, y0)
                mxall = max(mxall, mx)
    print(mxall)
