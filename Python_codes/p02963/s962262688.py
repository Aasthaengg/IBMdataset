S = int(input())

# (X1, Y1) は原点
# (X2, Y2) = (10 ** 9, 1)
# S = 10 ** 9 * Y3 - X3

Y3 = (S + 10 ** 9 - 1) // (10 ** 9)
X3 = Y3 * (10 ** 9) - S

print(0, 0, 10 ** 9, 1, X3, Y3)