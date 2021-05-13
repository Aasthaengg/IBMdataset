f=[0]*45
f[0]=f[1]=1

def fib(n):
    if n ==0 or n==1:
        return 1
    else:
        if f[n] == 0:
            f[n] = fib(n-1)+fib(n-2)
            return f[n]
        else:
            return f[n-1]+f[n-2]
n = int(input())
print(fib(n))
