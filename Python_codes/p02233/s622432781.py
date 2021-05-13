n=int(input())

a=[1]*45


def fib(n):
    if n==0 or n==1:
        return 1
    else:
        if a[n]==1:
            a[n]=fib(n-1)+fib(n-2)
            
        return a[n]
           
print(fib(n))


