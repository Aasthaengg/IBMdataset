H,W = [int(v) for v in input().split()]
area = [input() for _ in range(H)]

dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
dp[1][1] = 1

for h,row in enumerate(area,1):
    for w,cell in enumerate(row,1):
        if cell != '#':
            dp[h][w] += int((dp[h-1][w] + dp[h][w-1]) % (1e9 + 7))

print(dp[-1][-1])
