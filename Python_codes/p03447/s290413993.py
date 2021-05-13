x, a, b = [int(input()) for _ in range(3)]
n = (x - a) // b
print(x - a - b*n)