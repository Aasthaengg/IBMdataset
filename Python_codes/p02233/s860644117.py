#coding:utf-8
n = int(input())
F = [False for i in range(n+1)]
def fib(n):
    if n == 0 or n == 1:
        F[n] = 1
        return 1
    if F[n]:
        return F[n]
    F[n] = fib(n-2) + fib(n-1)
    return F[n]

a = fib(n)
print(a)

