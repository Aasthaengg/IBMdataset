a, b, x = map(int, input().split())

a = -(-a // x) * x
b = (b // x) * x
print(max(0, (b - a) // x + 1))