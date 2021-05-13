h, w = map(int, input().split())
lst = []
for _ in range(h):
    lst.append(list(input()))
    
MOD = 10**9 + 7
dp = [[0] * (w+1) for _ in range(h+1)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if i == 1 and j == 1:
            dp[i][j] = 1
        elif lst[i-1][j-1] == '.':
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
print(dp[h][w])