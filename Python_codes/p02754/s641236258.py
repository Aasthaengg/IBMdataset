n, a, b = map(int, input().split())

chunk = n // (a + b) * a
rest = a if n % (a + b) > a else n % (a + b)
print(chunk + rest)