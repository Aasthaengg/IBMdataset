n, k = map(int, input().split())
print((n - 1) // (k - 1) + (0 if (n - 1) % (k - 1) == 0 else 1))
