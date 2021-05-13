n, a, b = map(int, input().split())
x = list(map(int, input().split()))

#end = x[n - 1]
#lim = 10 ** 18
dp = [0] * n

pre = x[0]
for i in range(1, n):
    distance = x[i] - x[i - 1]
    dp[i] = min(distance * a, b)

ans = sum(dp)
print(ans)