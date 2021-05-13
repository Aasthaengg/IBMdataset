n = int(input())
h = list(map(int, input().split()))
dp = [0, abs(h[1] - h[0])]
for i in range(n - 2):
    a = dp[i] + abs(h[i + 2] - h[i])
    b = dp[i + 1] + abs(h[i + 2] - h[i + 1])
    dp.append(min(a, b))
print(dp[-1])