from collections import deque

n , m = map(int, input().split())
maze = [['#']+list(input())+['#'] for i in range(n)]
maze = [['#']*(m+2)]+maze+[['#']*(m+2)]

step = [(0,1),(1,0),(-1,0),(0,-1)]

costma=0
for i in range(1,n+1):
    for j in range(1,m+1):
        v = [[0]*(m+2) for i in range(n+2)]
        d = deque()
        d.append((i,j,0))
        v[i][j]=1
        while d:
            y,x,cost=d.popleft()
            if maze[y][x]=='.':
                for dy,dx in step:
                    if maze[y+dy][x+dx]=='.' and v[y+dy][x+dx]==0:
                        v[y+dy][x+dx]=1
                        d.append((y+dy,x+dx,cost+1))
                        costma=max(cost+1,costma)
print(costma)
