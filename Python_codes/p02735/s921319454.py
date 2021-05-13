H, W = map(int,input().split())
table = []
for h in range(H):
    table.append(input())

dp=[[1000 for i in range(W+1)] for j in range(H+1)]
dp[0][1] = 0
dp[1][0] = 0

for h in range(H):
    for w in range(W):
        dp[h+1][w+1] = min(
            dp[h][w+1] + (table[h][w]=='#' and (h==0 or table[h-1][w]=='.')),
            dp[h+1][w] + (table[h][w]=='#' and (w==0 or table[h][w-1]=='.'))
        )

print (dp[-1][-1])