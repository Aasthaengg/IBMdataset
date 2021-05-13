n, k = map(int, input().split())
h = list(map(int, input().split()))


def cost(x: int, y: int) -> int:
    global h
    return abs(h[x] - h[y])


dp = [10**9] * n
dp[0] = 0

for i in range(1, n):
    for j in range(k):
        d = i - j - 1
        if d < 0 or d > n:
            break
        dp[i] = min(dp[i], dp[d] + cost(i, d))
print(dp[n-1])
