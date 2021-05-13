x, a, b = (int(input()) for i in [0]*3)
y = x - a
k = y // b
print(x - a - b*k)