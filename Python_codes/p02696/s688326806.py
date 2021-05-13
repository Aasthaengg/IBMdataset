def f(x): return int(a * x / b) - a * int(x / b)
a, b, n = map(int, input().split())
print(f(min(b - 1, n)))
