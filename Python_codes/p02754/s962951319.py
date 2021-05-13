n, a, b = [int(_) for _ in input().split()]
print((n // (a + b)) * a + min(n % (a + b), a))