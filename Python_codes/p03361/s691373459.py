import sys
h,w=map(int,input().split())
s=[list(input()) for i in range(h)]

dp=[[0]*w for i in range(h)]

def dfs(x,y):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    if s[x][y]=="#":
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and s[nx][ny]=="#":
                dp[x][y]=1
for i in range(h):
    for j in range(w):
        dfs(i,j)
for i in range(h):
    for j in range(w):
        if s[i][j]=="#" and dp[i][j]==0:
            print("No")
            sys.exit()
print("Yes")