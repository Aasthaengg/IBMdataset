n, a, b = map(int, input().split())

x, y = divmod(n, a + b)
print(a * x + y if y <= a else a * (x + 1))