x, a, b = [int(input()) for _ in range(3)]

print(x - a - int((x - a)/ b) * b)