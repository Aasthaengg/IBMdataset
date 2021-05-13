N = int(input())
An = list(map(int, input().split()))
dp = [0 for x in range(N+10)]
An.insert(0, 0)
dp[1] = 1000
for i in range(2, N+1):
    stock = dp[i-1] // An[i-1]
#     print(dp[i-1], An[i-1], stock)
    money = dp[i-1]
    money -= stock * An[i-1]
    money += stock * An[i]
#     print(money)
    dp[i] = max(dp[i-1], money)
print(dp[N])






