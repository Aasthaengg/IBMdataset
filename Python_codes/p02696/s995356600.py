from math import floor
a, b, n = map(int, input().split())
def f(x):
    return floor(a*x/b) - a*floor(x/b)
print(f(min(n, b-1)))