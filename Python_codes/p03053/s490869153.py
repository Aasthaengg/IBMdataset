from collections import deque

h,w=map(int, input().split())
a = [input() for i in range(h)]
visited = [[-1]*w for i in range(h)]
black = []
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            black.append((i,j))
            visited[i][j] = 0

queue = deque(black)


while queue:
    y,x = queue.popleft()
    dydx = [[1,0],[-1,0],[0,1],[0,-1]]
    for j,k in dydx:
        newy,newx = y+j,x+k 
        if newy < 0 or newy >= h:continue 
        if newx < 0 or newx >= w:continue 
        if visited[newy][newx] == -1:
            visited[newy][newx] = visited[y][x] + 1
            queue.append((newy,newx))

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans,visited[i][j])

print(ans)
