# https://atcoder.jp/contests/abc129/tasks/abc129_c

n, m = map(int, input().split())
mod = 10 ** 9 + 7
broken = set()
for _ in range(m):
    broken.add(int(input()))

dp = [0 for _ in range(n + 1)]
dp[0] = 1
for i in range(n):
    for j in range(2):
        if i + 1 in broken:
            dp[i + 1] = 0
        else:
            if i - j >= 0:
                dp[i + 1] += dp[i - j] % mod

ans = dp[n] % mod
print(ans)
