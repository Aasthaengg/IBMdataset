inf = 1001001001
h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
dp = [[inf for j in range(w)] for j in range(h)]
if s[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0
for i in range(h):
    for j in range(w):
        if i+1 < h:
            count = dp[i][j]
            if s[i][j] == "." and s[i+1][j] == "#":
                count += 1
            dp[i+1][j] = min(dp[i+1][j], count)
        if j+1 < w:
            count = dp[i][j]
            if s[i][j] == "." and s[i][j+1] == "#":
                count += 1
            dp[i][j+1] = min(dp[i][j+1], count)
print(dp[h-1][w-1])