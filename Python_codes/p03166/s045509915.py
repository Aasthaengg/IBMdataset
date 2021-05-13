import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
def f(i, e, dp):
    if dp[i] is not None:
        return dp[i]
    val = 0
    for nxt in e[i]:
        val = max(val, f(nxt, e, dp) + 1)
    dp[i] = val
    return dp[i]


def edu_dp_g_longest_path():
    n, m = map(int, input().split())
    e = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        e[x - 1].append(y - 1)
    dp = [None] * n
    result = 0
    for i in range(n):
        result = max(result, f(i, e, dp))
    print(result)

edu_dp_g_longest_path()