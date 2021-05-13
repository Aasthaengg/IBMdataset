d, n = map(int, input().split())

print((100 ** d) * (n if n < 100 else n + 1))
