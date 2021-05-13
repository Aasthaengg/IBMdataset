h, w = map(int, input().split())
a = [["#"] * (w + 1)]
for _ in range(h):
    a.append(["#"] + list(input()))
mod = 10 ** 9 + 7

dp = [[0] * (w + 1) for _ in range(h + 1)]
for hi in range(1, h + 1):
    for wi in range(1, w + 1):
        if hi == 1 and wi == 1:
            dp[hi][wi] = 1
            continue
        if a[hi][wi] == ".":
            dp[hi][wi] = dp[hi-1][wi] + dp[hi][wi-1]
            dp[hi][wi] %= mod

ans = dp[h][w]
print(ans)
