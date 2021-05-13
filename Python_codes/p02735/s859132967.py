h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dp = [[h * w] * w for _ in range(h)]
dp[0][0] = 0 if s[0][0] == "." else 1

for x0 in range(w):
    for y0 in range(h):
        for i, j in [(0, 1), (1, 0)]:
            x = x0 + i
            y = y0 + j
            if x < w and y < h:
                n = 1 if s[y0][x0] == "." and s[y][x] == "#" else 0
                dp[y][x] = min(dp[y0][x0] + n, dp[y][x])

print(dp[-1][-1])
