# e get everything
n, m = map(int, input().split())

lists = []
for i in range(m):
    price, num = map(int, input().split())
    K = list(map(int, input().split()))
    cnt = 0
    for some in K:
        cnt += 2**(n - some)
    lists.append((price, cnt))

dp = [[10**10 for i in range(2**n)]for j in range(m + 1)]
# dp[i][j]=i番目までの鍵を使用してjの状態を再現するために必要な最小の値
dp[0][0] = 0
for i in range(1, m + 1):
    price, mode = lists[i - 1][0], lists[i - 1][1]
    for j in range(2**n):
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j &(2**n-1-mode)] + price)

ans = dp[m][2**n - 1]

if ans < 10**10:
    print(ans)
else:
    print(-1)
