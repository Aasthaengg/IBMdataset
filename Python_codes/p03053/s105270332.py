from collections import deque
h,w = map(int,input().split())
a = [list(input()) for i in range(h)]
visit = [[-1 for i in range(w)] for j in range(h)]
d = deque()

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            visit[i][j] = 0
            d.append((i,j))

p = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0
while d:
    x,y = d.popleft()
    for s,t in p:
        if 0 <= x+s <= h-1 and 0 <= y+t <= w-1:
            if visit[x+s][y+t] == -1:
                visit[x+s][y+t] = visit[x][y] + 1
                ans = max(ans,visit[x][y]+1)
                d.append((x+s,y+t))
        
print(ans)