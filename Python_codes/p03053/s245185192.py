import collections
INF = 10**18
h,w = map(int,input().split())
li = [list(input()) for i in range(h)]
koho = []
d = [[-1]*w for i in range(h)]
q = collections.deque([])
for i in range(h):
    for j in range(w):
        if li[i][j] == "#":
            d[i][j] = 0
            q.append([i,j])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while q:
    p = q.popleft()
    y = p[0]
    x = p[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<w and 0<=ny<h:
            if d[ny][nx] == -1:
                q.append([ny,nx])
                d[ny][nx] = d[y][x] + 1
ans = -1
for i in range(h):
    for j in range(w):
        ans = max(ans,d[i][j])
print(ans)