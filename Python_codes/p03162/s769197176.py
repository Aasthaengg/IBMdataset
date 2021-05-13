N = int(input())

table = [[0]*3 for i in range(N)]

for i in range(N):
    a = list(map(int,input().split()))
    for j in range(3):
        table[i][j] = a[j]


dp = [[0]*3 for i in range(N+1)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + table[i][k])

ans = 0            
for j in range(3):
    ans = max(ans,dp[N][j])
    
print(ans)