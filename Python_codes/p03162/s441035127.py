
n = int(input())

li = [ list(map(int,input().split())) for i in range(n) ]

dp = [[0 for i in range(3)] for j in range(n) ]

dp[0] = li[0]

for i in range(1,n):
    for j in range(0,3):
        for k in range(0,3):
            if k != j:
                if dp[i][k] < (dp[i-1][j] + li[i][k]):
                    dp[i][k] = dp[i-1][j] + li[i][k]

  
print(max(dp[-1]))