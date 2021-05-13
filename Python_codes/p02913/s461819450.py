n=int(input())
s=input()
dp=[(n+1)*[0]for _ in range(n+1)]
for i in range(1,n):
    for j in range(i+1,n+1):
        if s[i-1]==s[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        dp[i][j]=min(dp[i][j],i,j-i)
print(max(max(i)for i in dp))