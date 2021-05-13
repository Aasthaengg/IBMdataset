#input
H, W = map(int, input().split())
a = ["" * W for _ in range(H)]
for i in range(H):
    a[i] = list(map(str, input().split()))

#output
mod = 10**9 + 7

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

for j in range(W):
    if a[0][0][j] == ".":
        dp[0][j] = 1
    else:
        break
for i in range(H):
    if a[i][0][0] == ".":
        dp[i][0] = 1
    else:
        break

for i in range(H-1):
    for j in range(W-1):
        if a[i+1][0][j+1] == "#":
            dp[i+1][j+1] = 0
        else:
            dp[i+1][j+1] = dp[i+1][j] % mod + dp[i][j+1] % mod

print(dp[H-1][W-1] % mod)