n = int(input())
dp = [[0,0,0] for i in range(n)]
a,b,c = map(int,input().split())
dp[0][0],dp[0][1],dp[0][2] = a,b,c
for i in range(1,n):
    abc = list(map(int,input().split()))
    for j in range(0,3):
        for k in range(0,3):
            if k != j:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abc[j])
print(max(dp[n-1]))
