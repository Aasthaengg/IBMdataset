from collections import deque
h,w=map(int,input().split())
dist=[[-1]*(w+2) for _ in range(h+2)]
dist[1][1]=1
maze=[]
maze.append(['#' for _ in range(w+2)])
for i in range(h):
    maze.append(['#']+list(input())+['#'])
maze.append(['#' for _ in range(w+2)])
cnt=0
for i in range(h+2):
    for j in range(w+2):
        if maze[i][j]=='#':
            cnt+=1

d=[[-1,0],[1,0],[0,-1],[0,1]]
q=deque()
q.append([1,1])
while q:
    x,y=q.popleft()
    for dx,dy in d:
        if (0<=x+dx<=h+1) and (0<y+dy<w+1):
            if maze[x+dx][y+dy]==".":
                if dist[x+dx][y+dy]==-1 or dist[x+dx][y+dy]>dist[x][y]+1:
                    q.append([x+dx,y+dy])
                    dist[x+dx][y+dy]=dist[x][y]+1
if dist[h][w]==-1:
    print(-1)
else:
    print((h+2)*(w+2)-cnt-dist[h][w])