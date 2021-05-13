H,W = map(int,input().split())
dp = [[0]*(W+1) for _ in range(H+1)]
Map = []
for _ in range(H):
    line = list(input())
    Map.append(line)
MOD = 10**9+7
dp[1][1]=1
for i in range(H):
    for j in range(W):
        if Map[i][j]=='#':
                dp[i][j]=0
        else:
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%MOD
            
            dp[i+1][j+1]+=(dp[i][j+1]+dp[i+1][j])%MOD
print(dp[-1][-1])