n, a, b = map(int, input().split())
tot = a + b
div, mod = divmod(n, tot)
if mod >= a:
    print(a * div + a)
else:
    print(a * div + mod)
