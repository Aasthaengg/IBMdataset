n = int(input())
memo = [-1 for i in range(n+1)]

def fib(n):
    if n == 0 or n == 1:
        memo[n] = 1
        return memo[n]
    if memo[n] >= 0:
        return memo[n]
    memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]

print(fib(n))
