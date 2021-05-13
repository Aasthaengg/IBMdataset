N,M=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))

data=[[0 for i in range(0,M)] for j in range(0,N)]
for i in range(0,N):
    if S[i]==T[0]:
        data[i][0]=1

dp=[[1 for i in range(0,M)] for j in range(0,N)]
for j in range(0,M):
    if j==0:
        if S[0]==T[0]:
            dp[0][0]=2
    else:
        if S[0]==T[j]:
            dp[0][j]=(dp[0][j-1]+1)%(10**9+7)
        else:
            dp[0][j]=dp[0][j-1]%(10**9+7)

for i in range(0,N):
    for j in range(0,M):
        if j!=0:
            if S[i]==T[j]:
                data[i][j]=(data[i][j-1]+dp[i-1][j-1])%(10**9+7)
            else:
                data[i][j]=data[i][j-1]
        if i!=0:
            dp[i][j]=(dp[i-1][j]+data[i][j])%(10**9+7)

print(dp[N-1][M-1]%(10**9+7))