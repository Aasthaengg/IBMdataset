n = int(input())

dp = [0]*(45)
dp[0] = 1
dp[1] = 1
def fib(i):
    j = 2
    while j <= i:
        if j >= 2:
            dp[j] = dp[j-1] + dp[j-2]
        j += 1

fib(n)
print(dp[n])

