def fib(n):
    if n == 0 or n == 1:
        return 1
    if A[n] is not None:
        return A[n]
    A[n] = fib(n - 1) + fib(n - 2)
    return A[n]


A = [None] * (44 + 1)
n = int(input())
print(fib(n))