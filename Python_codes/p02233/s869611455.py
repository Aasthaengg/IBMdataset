def fib(n):
    global F
    if n not in F:
        F[n] = fib(n-1)+fib(n-2)
    return F[n]

F = {0:1,1:1}
print(fib(int(input())))
