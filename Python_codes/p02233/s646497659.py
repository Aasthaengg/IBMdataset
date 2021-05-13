n = int(input())

def Fib(n):
    a, b = 0, 1
    if n == 0:
        return a + 1
    elif n == 1:
        return b
    else:
        for i in range(n):
            a, b = b, a + b
        return b

print(Fib(n))
