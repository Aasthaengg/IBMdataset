n, m = map(int, input().split())
n += 1
s = list(input())
dp = [0] * n
for i in range(1, n):
    if i - m < 0 and s[n - i - 1] == "0":
        dp[i] = 1
    elif s[n - i - 1] == "1":
        dp[i] = -1
    else:
        for j in range(i - m, i):
            if not dp[j] == -1:
                dp[i] = dp[j] + 1
                break
t = [0] * n
j = 0
x = dp[n - 1] + 1
for i in range(n - 1, -1, -1):
    if dp[i] == x - 1:
        t[j] = i
        j += 1
        x -= 1
    elif dp[i] == 0:
        print(-1)
        exit()
ans = [t[i] - t[i + 1] for i in range(j - 1)]
print(*ans)