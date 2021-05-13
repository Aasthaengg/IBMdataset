a, b = map(int, input().split())

x = sorted([a, b, a - 1, b - 1], reverse=True)

print(x[0] + x[1])
