N = int(input())
X = [0]*45
def fib(n):
    while 1:
        if n ==0 or n==1:
            return 1
        else:
            if X[n] != 0:
                return X[n]
            else:
                X[n] =fib(n-1)+fib(n-2)
            return X[n]


print(fib(N))
