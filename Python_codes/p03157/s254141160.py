from collections import deque
h,w=map(int,input().split())
s=[input() for _ in range(h)]
visited=[[True]*w for _ in range(h)]
def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited[sx][sy]=False
    black=1
    white=0
    while q:
        x,y=q.popleft()
        for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx,ny=x+dx,y+dy
            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny]:
                    if s[x][y]=="#" and s[nx][ny]==".":
                        visited[nx][ny]=False
                        q.append((nx,ny))
                        white+=1
                    elif s[x][y]=="." and s[nx][ny]=="#":
                        visited[nx][ny]=False
                        q.append((nx,ny))
                        black+=1
    return black,white
ans=0
for sx in range(h):
    for sy in range(w):
        if s[sx][sy]=="#" and visited[sx][sy]:
            black,white=bfs(sx,sy)
            ans+=black*white
print(ans)