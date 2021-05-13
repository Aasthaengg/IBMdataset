N=int(input())
L=[]
for i in range(N):
    a,b,c=map(int,input().split())
    L.append([a,b,c])

dp=[[0]*N for _ in range(3)]
dp[0][0]=L[0][0]
dp[1][0]=L[0][1]
dp[2][0]=L[0][2]

for j in range(1,N):
    dp[0][j]=max(dp[1][j-1],dp[2][j-1])+L[j][0]
    dp[1][j]=max(dp[0][j-1],dp[2][j-1])+L[j][1]
    dp[2][j]=max(dp[0][j-1],dp[1][j-1])+L[j][2]

print(max(dp[0][N-1],dp[1][N-1],dp[2][N-1]))