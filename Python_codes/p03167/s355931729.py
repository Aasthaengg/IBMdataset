from sys import stdin
h,w = map(int,stdin.readline().split())
arr = [list(stdin.readline()) for _ in range(h)]
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
mod = 10**9+7
for i in range(h):
    for j in range(w):
        if arr[i][j] == '.':
            dp[i][j] += (0 if i==0 else dp[i-1][j])+(0 if j==0 else dp[i][j-1])
            dp[i][j] %= mod
print(dp[-1][-1])