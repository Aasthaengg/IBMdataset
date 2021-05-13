n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n+1)]
 
for i in range(n):
    abc = list(map(int, input().split(" ")))
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i+1][j] = max(dp[i+1][j], dp[i][k] + abc[j])

print(max(dp[-1]))