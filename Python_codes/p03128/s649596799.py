import resource
import sys
sys.setrecursionlimit(20000)
f = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n, m = map(int, input().split())
a = list(map(int, input().split()))

memo = ["-1"] * 10100


def MAX(x, y):
    if y[0] != '#' and (x == "#" or len(x) < len(y) or (len(x) == len(y) and x < y)):
        return y
    else:
        return x


def dp(i):
    # i本のマッチを使って作れる最大の整数
    if i < 0:
        return "#"

    if memo[i] != "-1":
        return memo[i]

    if i == 0:
        return ""

    ret = "#"
    for x in a:
        ret = MAX(ret, dp(i - f[x]) + str(x))
    memo[i] = ret
    return ret


print(dp(n))
