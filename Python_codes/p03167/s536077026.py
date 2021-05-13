import sys
input=sys.stdin.readline

def grid(y,x,mp):
    mod=10**9+7
    dp=[[0]*x for _ in range(y)]
    dp[0][0]=1
    for h in range(y):
        for w in range(x):
            if mp[h][w]=='.':
                if 1<=h<y and 1<=w<x:
                    dp[h][w]=((dp[h][w-1]+dp[h-1][w])%mod)
                elif h==0 and 1<=w<x:
                    dp[h][w]=(dp[h][w-1]%mod)
                elif 1<=h<y and w==0:
                    dp[h][w]=(dp[h-1][w]%mod)
    return dp[y-1][x-1]


H,W=map(int,input().split())
mp=[list(input()) for _ in range(H)]
print(grid(H,W,mp))