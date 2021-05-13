a,b = map(int,input().split())
c = list(map(int,input().split()))
dp = [float("inf") for i in range(a+2)]
dp[0]=0
for i in range(a+1):
    for j in c:
        if i + j <= a:
            dp[i+j] = min(dp[i+j],dp[i] + 1)
            
print(dp[a])
            
        
