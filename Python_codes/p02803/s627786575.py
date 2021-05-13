from collections import deque

H, W = map(int, input().split())
S = [[i for i in input()] for j in range(H)]

dir = [[1,0], [-1,0], [0,1], [0,-1]]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#": continue
        ls = deque([[i, j]])
        dp = [[float("inf") for k in range(W)] for l in range(H)]
        dp[i][j] = 0
        while len(ls) > 0:
            x, y = ls.popleft()

            for dx, dy in dir:
                if x+dx < 0 or H-1 < x+dx: continue
                if y+dy < 0 or W-1 < y+dy: continue
                if S[x+dx][y+dy] == "#" or dp[x+dx][y+dy] != float("inf"): continue
                if dp[x+dx][y+dy] > dp[x][y] + 1:
                    dp[x+dx][y+dy] = dp[x][y] + 1
                    ls.append([x+dx,y+dy])

        for h in range(H):
            for w in range(W):
                if dp[h][w] == float("inf"): continue
                ans = max(ans, dp[h][w])

print(ans)