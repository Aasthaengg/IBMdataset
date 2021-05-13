n,m = map(int,input().split())
dp = [-1]*(n+1) 
dp[0] = 1
mod = 10**9 + 7
for i in range(m):
    a = int(input())
    dp[a-1] = 0
#print(dp)
for i in range(1,n+1):
    if dp[i] == 0:
        continue
    else:
        if i == 1:
            dp[i] = dp[i-1] +1
        else:
            dp[i] = (dp[i-1] + dp[i-2])%mod
        #print(dp)
print(dp[n-1])