def factorial(n):
    if n == 1:
        return 1
    else:
        return n + factorial(n - 1)


a, b = map(int, input().split())

diff = b - a

print(factorial(diff - 1) - a)