from collections import deque

h,w=map(int,input().split())
s=[list(input()) for i in range(h)]

q=deque()
ans=0

def bfs(i,j):
    global ans
    white=0
    black=0
    q.append((i,j))
    while q:
        y,x=q.popleft()
        if s[y][x]=='#':
            black+=1
        if s[y][x]=='.':
            white+=1
        for dy,dx in ((1,0),(0,1),(-1,0),(0,-1)):
            ny = y+dy
            nx = x+dx
            if 0<=ny<h and 0<=nx<w and s[y][x]!=s[ny][nx] and field[ny][nx]==False:
                field[ny][nx]=True
                q.append((ny,nx))
    ans+=(black*white)

field=[[False]*w for j in range(h)]                         
for i in range(h):
    for j in range(w):
        if s[i][j]=='.' and field[i][j]==False:
            field[i][j]=True
            bfs(i,j)

print(ans)