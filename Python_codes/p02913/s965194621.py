n, s = int(input()), input()
dp = [0] * (n + 1)
ans = 0
for i in range(n):
    for j in range(n - 1, i, -1):
        if s[i] == s[j]:
            dp[j + 1] = min(dp[j] + 1, j - i)
        else:
          dp[j + 1] = 0
    ans = max(max(dp), ans)
print(ans)