H,W = map(int,input().split())
dp = [list(input())for i in range(H)]
mod = 10**9+7
'''
dp = [[0]*(W) for i in range(H)]

dp[0][0] = 1
dp[1][0] = 1 if maze[1][0] != '#' else float('inf')
dp[0][1] = 1 if maze[1][0] != '#' else float('inf')

for i in range(H):
    for j in range(W):
        if 0 <= i+1 < H and 0 <= j+1 < W and maze[i+1][j] != '#':
            dp[i+1][j+1] += dp[i+1][j] % mod
        if 0 <= j+1 < W and 0 <= i+1 < H and maze[i][j+1] != '#':
            dp[i+1][j+1] += dp[i][j+1] % mod
print(dp[H-1][W-1] % mod) if dp[H-1][W-1] != float('inf') else 0
'''
dp[0][0] = 1
'''
dp[0][1] = 1 if dp[0][1] != '#' else '#'
dp[1][0] = 1 if dp[1][0] != '#' else '#'
'''
for i in range(H):
    for j in range(W):
        if dp[i][j] != '#' and j > 0 and isinstance(dp[i][j-1], int):
            if isinstance(dp[i][j], int):
                dp[i][j] += dp[i][j-1] % mod
            else:
                dp[i][j] = dp[i][j-1] % mod
        if dp[i][j] != '#' and i > 0 and isinstance(dp[i-1][j], int):
            if isinstance(dp[i][j],int):
                dp[i][j] += dp[i-1][j] % mod
            else:
                dp[i][j] = dp[i-1][j] % mod
'''
print(dp)
'''
print(dp[H-1][W-1] % mod) if dp[H-1][W-1] != '.' else print(0)

        
