n, m = map(int, input().split())
inf = 10 ** 10
dp = [inf for _ in range(2 ** n)]
dp[0] = 0
bin_s = [2 ** i for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    clst = list(map(int, input().split()))
    tmp = 2 ** n - 1
    for c in clst:
        tmp -= bin_s[c - 1]
    for i in range(2 ** n):
        dp[i] = min(dp[i], dp[i & tmp] + a)

if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])