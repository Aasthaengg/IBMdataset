n = int(input())
s = input()

dp = [[0]*(n+1) for _ in range(n+1)]


for i in reversed(range(n-1)):
    for j in reversed(range(i+1, n)):
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j+1]+1


ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        x = min(dp[i][j], j-i)
        if ans < x:
            ans = x
print(ans)
