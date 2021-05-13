n = int(input())
s = input()
dp = [[0]*(n) for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if i == (n-1):
            if s[i] == s[j]:
                dp[i][j] += 1
            continue

        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j+1] + 1        

ans = 0
for i in range(n-1, -1, -1):
    for j in range(i, -1, -1):
        ans = max(ans, min(abs(j-i), dp[i][j]))
print(ans)