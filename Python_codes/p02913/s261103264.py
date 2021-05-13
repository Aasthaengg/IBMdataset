n = int(input())
s = input()
dp = [[0]*5005 for _ in range(5005)]
for i in range(n)[::-1]:
    for j in range(n)[::-1]:
        if s[i]!=s[j]:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i+1][j+1] + 1
ans = 0
for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        now = min(dp[i][j], j-i)
        ans = max(ans, now)
print(ans)