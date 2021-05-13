import sys
sy=sys.stdin.readline

n=int(sy())
if n==1:
    print(1)
    quit()
dp=[0]*(n+1)
lis=[0]*(2*10**5+1)
dp[0],dp[1],dp[2]=0,1,1
c1=int(sy())
c2=int(sy())
lis[c1]=1
lis[c2]=2
for i in range(3,n+1):
    c1=c2
    c2=int(sy())
    if c1==c2 or lis[c2]==0:
        dp[i]=dp[i-1]
    else:
        dp[i]=dp[i-1]+dp[lis[c2]]
    lis[c2]=i
    dp[i]%=1000000007
print(dp[n])