H, W = map(int, input().split())
S = ["."*(W+1)]+["."+input() for _ in range(H)]

dp = [[0]*(W+1) for _ in range(H+1)]
for h in range(H+1):
    dp[h][0] = H*2
for w in range(W+1):
    dp[0][w] = W*2
dp[0][1] = 0

for h in range(1, H+1):
    for w in range(1, W+1):
        dp[h][w] = min(dp[h-1][w]+(S[h][w]!=S[h-1][w]), dp[h][w-1]+(S[h][w]!=S[h][w-1]))

print((dp[-1][-1]+1)//2)