def fib(n):
    fib = [1,1]
    for i in range(2,n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n]
    
n=int(input())
print(fib(n))
