f=[None for i in range(45)]

def fib(n):
    if n==0 or n==1:
        if f[n] is None:
            f[n] = 1
        return 1
    else:
        if f[n-2] is not None:
            f_n_2 = f[n-2]
        else:
            f_n_2 = fib(n-2)
            f[n-2] = f_n_2
        if f[n-1] is not None:
            f_n_1 =  f[n-1]
        else:
            f_n_1 = fib(n-1)
            f[n-1] = f_n_1
        f[n] = f_n_1 + f_n_2
        return f[n]
n = int(input())
print(fib(n))
