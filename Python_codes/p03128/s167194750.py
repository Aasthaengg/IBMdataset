import resource
import sys
sys.setrecursionlimit(20000)
f = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n, m = map(int, input().split())
a = list(map(int, input().split()))

memo = [-1]*10100


def dp(i):
    # i本のマッチを使って作れる最大の整数
    if i < 0:
        return - 10 ** 100000
    if not (0 <= i and i < 10100):
        print(-1)
        exit()
    if memo[i] != -1:
        return memo[i]
    if i == 0:
        return 0
    ret = -10**100000
    for x in a:
        ret = max(ret, 10 * dp(i - f[x]) + x)
    memo[i] = ret
    return ret


print(dp(n))
