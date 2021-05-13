n, a, b = map(int, input().split())
r = n // (a + b)
q = n % (a + b)
print(a * r + min(q, a))
