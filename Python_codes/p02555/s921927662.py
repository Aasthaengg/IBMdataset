S = int(input())
mod = 10 ** 9 + 7

dp = [1, 0, 0]
cnt = 0
for i in range(3, S+1):
    cnt = dp[i-1] + dp[i-3]
    cnt %= mod
    dp.append(cnt)

ans = dp[S]
print(ans)