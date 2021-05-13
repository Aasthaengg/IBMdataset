x, a, b = [int(input()) for _ in range(3)]

x -= a
while x >= b:
    x -= b
print(x)