def solve():
    for i in range(1, n):
        if i == 1:
            dp[i] = abs(lst[i] - lst[i-1]) + dp[i-1]
        else:
            dp[i] = min(abs(lst[i] - lst[i-1]) + dp[i-1], abs(lst[i] - lst[i-2]) + dp[i-2])


inf = 1<<60
n = int(input())
lst = list(map(int, input().split()))
dp = [inf] * (n+1)
dp[0] = 0
solve()
print(dp[n-1])

