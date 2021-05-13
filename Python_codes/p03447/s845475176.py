x = [int(input()) for _ in range(3)]
b = x[0] - x[1]
a = int(b / x[2])
print(b - (x[2] * a))
