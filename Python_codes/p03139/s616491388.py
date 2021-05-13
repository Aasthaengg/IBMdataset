n, a, b = map(int, input().split())

print(min(a, b),0 if (a + b) <= n else abs(b - (n - a)))
