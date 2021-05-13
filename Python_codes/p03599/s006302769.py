a, b, c, d, e, f = map(int,input().split())

dp = [[-1]*3 for _ in range(f + 1)]
dp[0] = [0, 0, 0]
for i in range(1, f+1):
    lst = []
    if i >= 100*a and dp[i-100*a][1] != -1:
        h = dp[i-100*a][2] / i
        lst.append([h, dp[i-100*a][1] + 100*a, dp[i-100*a][2]])
    if i >= 100*b and dp[i-100*b][1] != -1:
        h = dp[i-100*b][2] / i
        lst.append([h, dp[i-100*b][1] + 100*b, dp[i-100*b][2]])
    if i >= c and dp[i-c][1] > 0:
        h = (dp[i-c][2] + c) / i
        if h <= e/(100 + e):
            lst.append([h, dp[i-c][1], dp[i-c][2] + c])
    if i >= d and dp[i-d][1] > 0:
        h = (dp[i-d][2] + d) / i
        if h <= e/(100 + e):
            lst.append([h, dp[i-d][1], dp[i-d][2] + d])
    if lst:
        dp[i] = max(lst)
ans = max(dp)
print(ans[1] + ans[2], ans[2]) 