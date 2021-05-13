from math import gcd


def lgcd(x: list):
    res = x[0]
    for i in range(1, len(x)):
        res = gcd(res, x[i])

    return res


n, k = map(int, input().split())
a = list(map(int, input().split()))

m = max(a)
g = lgcd(a)

print(["IMPOSSIBLE", "POSSIBLE"][int(k % g == 0 and k <= m)])
