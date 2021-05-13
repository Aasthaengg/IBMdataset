def factorial(n, mod=10**9+7):
    a = 1
    for i in range(1,n+1):
        a = a * i % mod
    return a

print(factorial(int(input())))