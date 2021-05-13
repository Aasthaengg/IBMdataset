N,K=map(int,input().split())
A=list(map(int,input().split()))

dp=[[0 for i in range(0,2)] for i in range(0,K+1)]

dp[0][0]='Second'
dp[0][1]='First'

for i in range(1,K+1):
    ans='Second'
    for j in A:
        if i>=j and dp[i-j][1]=='First':
            ans='First'
    dp[i][0]=ans

    ans='First'
    for j in A:
        if i>=j and dp[i-j][0]=='Second':
            ans='Second'
    dp[i][1]=ans

print(dp[K][0])