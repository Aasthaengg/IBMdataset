memo={}
def fib(n) :
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    else :
        if n-1 not in memo:
            memo[n-1] = fib(n-1)
        if n-2 not in memo:
            memo[n-2] = fib(n-2)
        return memo[n-1] + memo[n-2]
n = int(input())
print(fib(n))
