n = int(input())
memo = [None]*(n+1)

def Fib(n):
    if n==0 or n==1:
        return 1
    elif memo[n]:
        return memo[n]
    else:
        r=Fib(n-1)+Fib(n-2)
        memo[n]=r
        return r
print(Fib(n))
