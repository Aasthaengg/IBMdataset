def factorial(n, mod):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
        fact %= mod
    return fact

N = int(input())
mod = 10 ** 9 + 7
print(factorial(N, mod))