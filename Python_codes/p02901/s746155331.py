n, m = map(int, input().split())

dp = [float('inf')] * (1 << n)
dp[0] = 0
for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))

    SS = sum([1 << (cc - 1) for cc in c])
    for S in range(1 << n):
        dp[S | SS] = min(dp[S | SS], dp[S] + a)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
