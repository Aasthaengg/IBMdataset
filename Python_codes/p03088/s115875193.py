# coding: utf-8
# Your code here!
N=int(input())

dp=[[[[0]*5 for i in range(5)] for j in range(5)] for k in range(N+1)]
dp[0][0][0][0]=1
#A:1 G:2 C:3 T:4
#AGC GAC ACG
#A?GC AG?C
for n in range(N):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                dp[n+1][j][k][1]+=dp[n][i][j][k]
                dp[n+1][j][k][2]+=0 if (j==1 and k==3) else dp[n][i][j][k]
                dp[n+1][j][k][3]+=0 if (i==1 and k==2) or (i==1 and j==2) or (j==1 and k==2) or (j==2 and k==1) else dp[n][i][j][k]
                dp[n+1][j][k][4]+=dp[n][i][j][k]
ans=0
for item in dp[N]:
    for jtem in item:
        ans+=sum(jtem)
print(ans%(10**9+7))
