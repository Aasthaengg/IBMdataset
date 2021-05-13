# https://atcoder.jp/contests/arc102/tasks/arc102_a

n, k = map(int, input().split())

dp = [0] * k

for i in range(1, n + 1):
    m = i % k
    dp[m] += 1
ans = dp[0] ** 3
if k % 2 == 0:
    ans += dp[k // 2] ** 3
print(ans)