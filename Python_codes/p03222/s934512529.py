from functools import lru_cache

mod = 10 ** 9 + 7

h, w, k = map(int, input().split())
k -= 1


@lru_cache(maxsize=w + 10)
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    # 縦線n本のあみだくじのパターン数
    # 右端の縦線を引くかどうかで漸化式を作る


dp = [0] * w
dp[0] = 1
ndp = [0] * w

for _ in range(h):
    for i in range(w):
        ndp[i] += dp[i] * fib((i + 1) - 1) * fib(w - (i + 1))  # 真下
        ndp[i] %= mod
        if i - 1 >= 0:
            ndp[i - 1] += dp[i] * fib((i + 1) - 2) * fib(w - (i + 1))  # 左
            ndp[i - 1] %= mod
        if i + 1 < w:
            ndp[i + 1] += dp[i] * fib((i + 1) - 1) * fib(w - (i + 1) - 1)  # 右
            ndp[i + 1] %= mod
    dp = ndp
    ndp = [0] * w
print(dp[k])
