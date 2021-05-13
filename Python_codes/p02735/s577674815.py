H,W = map(int, input().split())
g = []
for _ in range(H):
    g.append(list(input()))

dp = [[10**9 for _ in range(W)] for __ in range(H)]

dp[0][0] = 1 if g[0][0] == '#' else 0
d = ([0,1], [1,0])
for ix in range(H):
    for jx in range(W):
        for dx,dy in d:
            ni = ix + dx
            nj = jx + dy
            if ni >= H or nj >= W:
                continue
            add = 0
            if g[ix][jx] == '.' and g[ni][nj] == '#':
                add += 1
            dp[ni][nj] = min(dp[ni][nj], dp[ix][jx] + add)


print(dp[H-1][W-1])