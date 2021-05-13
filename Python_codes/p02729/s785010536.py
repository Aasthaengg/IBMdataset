n, m = map(int, input().split())

def factorial(n):
    v = 1
    for i in range(1, n + 1):
        v *= i
    return v

def comb(a, b):
    return factorial(a) // (factorial(b) * factorial(a - b))

if (n < 2) & (m < 2):
    print('0')
elif n < 2:
    print(comb(m, 2))
elif m < 2:
    print(comb(n, 2))
else:
    print(comb(n, 2) + comb(m, 2))