from collections import defaultdict
N, Ma, Mb = map(int, input().split())
INF, MAX = 1000000000, 10 * N + 1
dp = defaultdict(lambda : INF)
dp[(0, 0)] = 0
for i in range(N):
    a, b, c = map(int, input().split())
    predp = dp.copy()
    for ab, v in predp.items():
        _a, _b = ab
        dp[(_a+a, _b+b)] = min(dp[(_a+a, _b+b)], v+c)
ans = INF
for i in range(1, N+1):
    ans = min(ans, dp[(Ma*i, Mb*i)])
ans = -1 if ans == INF else ans
print(ans)
