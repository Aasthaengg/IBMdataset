n = int(input())
ans = 0
dp = [False for _ in range(10001)]
dp[0] = True
for _ in range(n):
    s = int(input())
    for i in range(10001, s - 1, -1):
        if dp[i - s]:
            dp[i] = True
            if i % 10 != 0:
                ans = max(ans, i)
print(ans)