import sys

sys.setrecursionlimit(10 ** 6)

inf = 10 ** 4


def larger(x, y):
    lx, ly = len(x), len(y)
    if lx > ly:
        return x
    elif lx < ly:
        return y
    else:
        x.sort(reverse=True)
        y.sort(reverse=True)
        for xx, yy in zip(x, y):
            if xx > yy:
                return x
            elif xx < yy:
                return y
        return x


def dfs(rest):
    if memo[rest] is not None:
        return memo[rest]

    res = []
    for use, number in d.items():
        if rest - use >= 0 and dp[rest - use] == dp[rest] - 1:
            res = larger(res, [number] + dfs(rest - use))

    memo[rest] = res
    return res


n, m = map(int, input().split())
a = tuple(map(int, input().split()))

needs = [inf, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# needs[i] : 数字iを作るのに必要なマッチの本数

for i in range(1, 10):
    if i not in a:
        needs[i] = inf

d = {needs[i]: i for i in range(1, 10) if needs[i] != inf}
# d[本数] = その本数で作れる最大の数値

dp = [-inf] * (n + 1)
dp[0] = 0
# dp[j] : j本から構成できる桁数の最大値

for j in range(2, n + 1):
    for use, number in d.items():
        if j - use >= 0:
            dp[j] = max(dp[j], dp[j - use] + 1)

# print(dp)

memo = [None] * (n + 1)

ans = dfs(n)
ans.sort(reverse=True)
print(*ans, sep='')