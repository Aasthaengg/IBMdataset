def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if F[n] > 0:
        return F[n]
    F[n] = fib(n-1) + fib(n-2)
    return F[n]

n = int(input())
F = [0 for i in range(n+1)]
print(fib(n))