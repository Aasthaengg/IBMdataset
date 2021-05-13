s=input()
n=len(s)
mod=10**9+7
dp=[[0]*3 for i in range(n)]
data=[0]*(n)
data[0]=1
for i in range(1,n):
    data[i]=data[i-1]*3%mod
count=0
if s[0]=="A":
    dp[0][0]=1
if s[0]=="?":
    dp[0][0]=1
    count+=1
for i in range(1,n):
    if s[i]=="A":
        dp[i][0]=(dp[i-1][0]+data[count])%mod
        dp[i][1]=dp[i-1][1]
        dp[i][2]=dp[i-1][2]
    elif s[i]=="B":
        dp[i][0]=dp[i-1][0]
        dp[i][1]=(dp[i-1][1]+dp[i-1][0])%mod
        dp[i][2]=dp[i-1][2]
    elif s[i]=="C":
        dp[i][0]=dp[i-1][0]
        dp[i][1]=dp[i-1][1]
        dp[i][2]=(dp[i-1][2]+dp[i-1][1])%mod
    else:
        dp[i][0]=(3*dp[i-1][0]+data[count])%mod
        dp[i][1]=(3*dp[i-1][1]+dp[i-1][0])%mod
        dp[i][2]=(3*dp[i-1][2]+dp[i-1][1])%mod
        count+=1
print(dp[n-1][2])