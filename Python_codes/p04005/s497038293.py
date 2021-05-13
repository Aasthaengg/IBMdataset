a, b, c = map(int, input().split())

x = sorted([a, b, c])
print(x[0] * x[1] * -(-x[2] // 2) - x[0] * x[1] * (x[2] // 2))