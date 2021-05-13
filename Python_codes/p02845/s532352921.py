n = int(input())
arr = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 3
ans = 1
for x in arr:
    ans *= dp[x]
    dp[x] -= 1
    dp[x + 1] += 1
    ans %= MOD

print(ans)