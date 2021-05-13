mod=1e9+7
def addself(a):
    if(a<mod):
        return a
    else:
        return (a+mod)%mod
    
n,m=map(int,input().split())
x = []
dp = [[0 for i in range(m+1)] for j in range(n+1)]
dp[1][1] = 1
for i in range(n):
    l = list(input())
    x.append(l)
for i in range(1,n+1):
    for j in range(1,m+1):
        if i ==1 and j==1:
            continue
        if x[i-1][j-1]=='#':
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]

        dp[i][j]=addself(dp[i][j])
            
print(int(dp[-1][-1]))
