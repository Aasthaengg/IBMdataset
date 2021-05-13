n, k = map(int, input().split())
r, s, p = map(int, input().split())

rsp = {'r':0, 's':1, 'p':2}
t = [rsp[c] for c in input()]
point = [p, r, s]

dp = [[0] * n for _ in range(3)] # 0:r, 1:s, 2:p
if n <= k:
    ans = sum(point[i] for i in t)
else:
    for i in range(k):
        dp[t[i]][i] = point[t[i]]
    for i in range(k, n):
        for j in range(3):
            dp[j][i] = max(dp[(j+1) % 3][i-k], dp[(j+2) % 3][i-k])
            if j == t[i]:
                dp[j][i] += point[j]
    ans = 0
    for i in range(k):
        ans += max(dp[j][-1-i] for j in range(3))
print(ans)
