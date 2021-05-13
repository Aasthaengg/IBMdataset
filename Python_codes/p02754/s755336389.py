n, a, b = map(int, input().split())
s = n // (a + b)
t = n % (a + b)
print(s * a + min(t, a))