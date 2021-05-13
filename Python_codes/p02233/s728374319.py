def fib(n,memo={}):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
        
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
a=int(input())
print(fib(a))
