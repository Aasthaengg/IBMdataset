from math import floor

def f(x):
    return floor(a * x / b) - a * floor(x / b)

a, b, n = (int(x) for x in input().split())
if n < b:
    print(f(n))
else:
    print(f(b - 1))