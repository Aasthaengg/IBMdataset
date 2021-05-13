H,W= map(int, input().split())
a=[list(input()) for i in range(H)]

dp=[[0 for i in range(W+1)] for j in range(H+1)]
dp[0][1]=1
for i in range(1,W+1):
    for j in range(1,H+1):
        if a[j-1][i-1]=='.':
            dp[j][i]=dp[j-1][i]+dp[j][i-1]
print((dp[-1][-1])%(10**9+7))