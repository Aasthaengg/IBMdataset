import sys

sys.setrecursionlimit(10**7)
h,w = map(int,input().split())
s = [list(input()) for i in range(h)]

dp = [[-1]*w for i in range(h)]

co = [0]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y,c):
    count = 0
    dp[x][y] = 1
    if s[x][y] == "#":
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "." and dp[nx][ny] == -1:
                count += 1
                count += dfs(nx,ny,c+1)
    elif s[x][y] == ".":
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "#" and dp[nx][ny] == -1:
                l.append((nx,ny))
                count += dfs(nx,ny,c+1)
    return count
            
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            l = []
            count = dfs(i,j,0)
            ans += count*(len(l)+1)
            s[i][j] = "x"
            for x,y in l:
                s[x][y] = "x"
print(ans)
            
        
    
    
