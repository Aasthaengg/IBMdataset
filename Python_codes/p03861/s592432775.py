a, b, x = map(int, input().split())
b //= x
a = (a - 1) // x
print(b - a)