n, m = map(int, input().split())
print((n - 2 if n > 1 else 1) * (m - 2 if m > 1 else 1))