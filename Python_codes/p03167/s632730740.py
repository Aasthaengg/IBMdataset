import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def grid(y,x):
    global dp,visited
    if visited[y][x]:
        return dp[y][x]
    else:
        visited[y][x]=True
        if mp[y][x]!='#' and dp[y][x]==0:
            dp[y][x]=(grid(y-1,x)+grid(y,x-1))%mod
        return dp[y][x]

H,W=map(int,input().split())
mp=[['#']*(W+1)]
for _ in range(H):
    mp.append(['#']+list(input()))

dp=[[0]*(W+1)for _ in range(H+1)]
dp[1][1]=1
visited=[[False]*(W+1)for _ in range(H+1)]
mod=10**9+7
grid(H,W)
print(dp[H][W])
