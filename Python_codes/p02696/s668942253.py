a, b, n = map(int, input().split())

def f(x):
    return ((a * x) // b) - (a * (x // b))

if n < b - 1:
    max = f(n)
elif b == 1:
    max = 0
else:
    x = b - 1
    max = f(x)
    while x <= n:
        if max < f(x):
            max = f(x)
        x += b

print(max)