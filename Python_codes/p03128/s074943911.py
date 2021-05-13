import collections
import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]

d0 = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

n, m = ril()
ls = ril()

d = collections.defaultdict(int)
for x in ls:
    d[d0[x]] = max(x, d[d0[x]])

dp = [(0, 0)] * (n + 1)
for i in range(2, n + 1):
    for count, num in d.items():
        if count > i:
            continue
        k, l = dp[i - count]
        if count != i and l == 0:
            continue
        dp[i] = (max(dp[i][0], 10 * k + num), max(dp[i][1], l + 1))
        if k != 0:
            dp[i] = (max(dp[i][0], num * 10**l + k), max(dp[i][1], l + 1))
print(dp[n][0])