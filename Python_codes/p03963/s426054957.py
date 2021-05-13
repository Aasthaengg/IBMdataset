n, k = map(int, input().split())
print(k * (k - 1) ** (n - 1) if n > 1 else k)