h,n = map(int,input().split())
P = []
M = []

for i in range(n):
    p,m = map(int,input().split())  
    P.append(p)
    M.append(m)
    
dp=[[999999999]*(h+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(h+1):
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        dp[i+1][min(j+P[i],h)] = min(dp[i+1][min(j+P[i],h)],dp[i+1][j] + M[i] )
 
print(dp[n][h])