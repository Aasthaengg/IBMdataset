# coding=utf-8

def fib(n):
    global fib_list
    if fib_list[n]:
        return fib_list[n]

    if n == 0:
        fib_list[0] = 1
        return 1
    elif n == 1:
        fib_list[1] = 1
        return 1
    else:
        fib_list[n] = fib(n-2) + fib(n-1)
        return fib(n-2) + fib(n-1)

n = int(input())
fib_list = [None for i in range(n+1)]
print(fib(n))