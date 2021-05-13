h,w = map(int,input().split())
u = [list(input()) for _ in range(h)]
from collections import deque
q = deque([])
dist = [[-1 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if u[i][j]=='#':
            q.append((i,j))
            dist[i][j]=0

while q:
    (i,j) = q.popleft()
    if 0<=i-1<h:
        if u[i-1][j]=='.' and dist[i-1][j]==-1:
            u[i-1][j]='#'
            q.append((i-1,j))
            dist[i-1][j]=dist[i][j]+1
    if 0<=i+1<h:
        if u[i+1][j]=='.' and dist[i+1][j]==-1:
            u[i+1][j]='#'
            q.append((i+1,j))
            dist[i+1][j]=dist[i][j]+1
    if 0<=j-1<w:
        if u[i][j-1]=='.' and dist[i][j-1]==-1:
            u[i][j-1]='#'
            q.append((i,j-1))
            dist[i][j-1]=dist[i][j]+1
    if 0<=j+1<w:
        if u[i][j+1]=='.' and dist[i][j+1]==-1:
            u[i][j+1]='#'
            q.append((i,j+1))
            dist[i][j+1]=dist[i][j]+1

z=[]
for b in dist:
    z.append(max(b))

print(max(z))