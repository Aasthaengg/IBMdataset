H,W = map(int,input().split())
S = [input() for _ in range(H)]

ans = 0
visited = [[0]*W for _ in range(H)]
stack = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(H):
    for j in range(W):
        b,w = 0,0
        if not visited[i][j]:
            stack.append([i,j])
            visited[i][j] = 1
            while stack:
                x,y = stack.pop()
                if S[x][y]=='#':
                    b += 1
                else:
                    w += 1
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if not(0<=nx<H and 0<=ny<W):
                        continue
                    if not visited[nx][ny] and S[x][y]!=S[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append([nx,ny])
            ans += b*w

print(ans)