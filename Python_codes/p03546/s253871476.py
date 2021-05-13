# 62


h, w = map(int, input().split())
dp = [[int(x) for x in input().split()] for y in range(10)]
a_l = [[int(x) for x in input().split()] for y in range(h)]

for k in range(10):
    for j in range(10):
        for i in range(10):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            
ans = 0
for i in range(h):
    for _a in a_l[i]:
        if _a == -1:
            continue
        ans += dp[_a][1]

print(ans)