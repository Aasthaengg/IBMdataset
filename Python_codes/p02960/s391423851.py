m=10**9+7
s=list(input())
n=len(s)
s.reverse()
dp=[[0]*13 for _ in range(n)]
if s[0]=="?":
    for i in range(10):
        dp[0][i]+=1
else:
    dp[0][int(s[0])]=1
x=1
for i in range(1,n):
    x=(x*10)%13
    for j in range(13):
        if s[i]=="?":
            if dp[i-1][j]!=0:
                for k in range(10):
                    dp[i][(j+k*x)%13]+=dp[i-1][j]
                    dp[i][j]%=m
        else:
            if dp[i-1][j]!=0:
                dp[i][(j+int(s[i])*x)%13]+=dp[i-1][j]
                dp[i][j]%=m
print(dp[n-1][5]%m)