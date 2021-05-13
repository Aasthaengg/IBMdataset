c, a, b = map(int, input().split())
print(int(min(a, b, c) * (a + b + c - min(a, b, c) - max(a, b, c)) / 2))