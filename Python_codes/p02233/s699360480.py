N = int(input())
x = [0]*(N+1)
def fibo(n):
    if n ==0 or n==1:
        return 1
    else:
        if x[n] != 0:
            return x[n]
        else:
            x[n] = fibo(n-1)+fibo(n-2)
            return x[n]
print(fibo(N))
