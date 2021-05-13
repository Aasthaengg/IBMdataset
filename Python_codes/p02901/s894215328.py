import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
items = []
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    c_ = sum([1 << (x - 1) for x in c])
    items.append([a, c_])

dp = [[float("inf")]*2**n for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = 0

for i in range(1, m + 1):
    a, c_ = items[i - 1]
    # 鍵を使わない
    for j in range(2**n):
        dp[i][j] = dp[i - 1][j]
    # 鍵を使うときと使わないときの比較
    for j in range(2**n):
        dp[i][j|c_] = min(dp[i][j|c_], dp[i - 1][j] + a)

ans = float("inf")

for i in range(1, m + 1):
    ans = min(ans, dp[i][-1])

if ans != float("inf"):
    print(ans)
else:
    print(-1)