s = int(input())
x, y = (s - 1) // pow(10, 9) + 1, s % pow(10, 9)
if y == 0:
    y = pow(10, 9)
print(1, 0, 0, pow(10, 9), x, y)