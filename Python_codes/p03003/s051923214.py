import sys
input = sys.stdin.readline

mod = 10**9+7
n,m= map(int, input().split())
s= list(map(int, input().split()))
t= list(map(int, input().split()))

# dp[i][j]:nからi番目までとtからj番目まで取ったときの共通部分整数列の組み合わせ
dp=[[1]*(m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i+1][j]+dp[i][j+1]
        else:
            dp[i+1][j+1]=dp[i+1][j]+dp[i][j+1]-dp[i][j]
        dp[i+1][j+1]%=mod

print(dp[n][m])