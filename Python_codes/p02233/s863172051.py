n = int(input())
dp = [None for _ in range(n+1)]

def fib(i):
    if dp[i] is not None:
        return dp[i]
    if i==0:
        return 1
    if i==1:
        return 1
    dp[i] = fib(i-1) + fib(i-2)
    return dp[i]

print(fib(n))
