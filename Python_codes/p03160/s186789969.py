n = int(input())
h_li = list(map(int, input().split()))

dp = [10**18] * n
dp[0] = 0
for i in range(1,n):
    if i == 1:
        dp[i] = abs(h_li[i] - h_li[0])
    else:
        dp[i] = min(abs(h_li[i] - h_li[i-1]) + dp[i-1], abs(h_li[i] - h_li[i-2]) + dp[i-2])

print(dp[-1])