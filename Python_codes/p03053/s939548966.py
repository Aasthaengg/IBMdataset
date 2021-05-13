import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = [input().rstrip() for _ in range(H)]
dp = [[float('inf') if A[i][j] == '.' else 0 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
for i in range(H)[::-1]:
    for j in range(W)[::-1]:
        if i < H-1:
            dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
        if j < W-1:
            dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
for i in range(H):
    for j in range(W)[::-1]:
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        if j < W-1:
            dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
for i in range(H)[::-1]:
    for j in range(W):
        if i < H-1:
            dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
print(max(max(row) for row in dp))
