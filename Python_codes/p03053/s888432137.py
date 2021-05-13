from collections import deque
 
h,w = map(int,input().split())
s = [None]*h
 
for i in range(h):
    s[i] = input()
 
d = [[10000000 for i in range(w)] for j in range(h)]
sharp = 0
 
sx = []
sy = []
            
dx = [1,0,-1,0]
dy = [0,1,0,-1]
 
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            sx.append(j)
            sy.append(i)
            d[i][j] = 0
            
            
def bfs():
    que = deque()
    ans = 0
    for i in range(len(sx)):
        que.append([sy[i],sx[i]])
    
    while que:
        y,x = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<=nx and nx<w and 0<=ny and ny<h and d[ny][nx] == 10000000:
                if d[ny][nx] > d[y][x]+1:
                    d[ny][nx] = d[y][x]+1
                    que.append([ny,nx])
                    
                    if d[ny][nx] > ans:
                        ans = d[ny][nx]
    
    print(ans)
        
bfs()