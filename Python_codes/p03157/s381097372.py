from collections import deque

h,w = map(int,input().split())
s = [list(input()) for i in range(h)]

used = [[0]*w for i in range(h)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0

for i in range(h):
    for j in range(w):
        if used[i][j]:
            continue
        cw = 0
        cb = 0
        q = deque([])
        q.append([i,j])
        used[i][j] = 1
        while q:
            x,y = q.popleft()
            if s[x][y] == "#":
                cb += 1
            else:
                cw += 1
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0 <= nx < h and 0 <= ny < w:
                    if (not used[nx][ny]) and s[x][y] != s[nx][ny]:
                        used[nx][ny] = 1
                        q.append([nx,ny])
        ans += cw*cb
print(ans)