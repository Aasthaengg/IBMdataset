def fib(memo,n):
    if n in memo:
        return memo[n]
    else:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            memo[n] = fib(memo,n-1)+fib(memo,n-2)
            return memo[n]

memo = {}
n = int(raw_input())
print fib(memo,n)