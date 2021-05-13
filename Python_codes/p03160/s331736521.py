def small(a, b):
    if a > b:
        return b
    else:
        return a


n = int(input())
h = list(map(int, input().split()))
INF = 10 ** 9
dp = [INF] * n
dp[0] = 0
for i in range(n):
    for j in range(1, 3):
        if i + j < n:
            dp[i + j] = small(dp[i + j], dp[i] + abs(h[i] - h[i + j]))
print(dp[-1])