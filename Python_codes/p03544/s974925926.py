n=int(input())
def Fib(n):
    a, b = 2, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b
print(Fib(n+1))