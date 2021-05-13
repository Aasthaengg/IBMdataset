from collections import deque
def bfs(sl, visited, sy, sx, h, w):
    q = deque([(sy,sx,sl[sy][sx])])
    visited[sy][sx] = 0
    bh_cnt = {'#':0, '.':0}
    bh_cnt[sl[sy][sx]] += 1
    while q:
        y, x, bh = q.popleft()
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ny, nx = y+j, x+k
            if ny >= h or nx >= w or ny < 0 or nx < 0:
                continue
            if sl[ny][nx] != bh and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                bh_cnt[sl[ny][nx]] += 1
                q.append((ny,nx,sl[ny][nx]))
    return bh_cnt['#']*bh_cnt['.']


h,w = map(int, input().split())
sl = []
for _ in range(h):
    row = list(input())
    sl.append(row)
visited = [ [-1]*w for i in range(h)]

ans = 0
for hi in range(h):
    for wi in range(w):
        if visited[hi][wi] != -1: continue
        ans += bfs(sl, visited, hi, wi, h, w)
print(ans)