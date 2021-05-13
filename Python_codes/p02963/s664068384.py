S = int(input())
M = 10 ** 9
X1 = 0
Y1 = 0
X2 = M
Y2 = 1
X3 = (M - S%M)%M
Y3 = (S + X3) // M
print(X1, Y1, X2, Y2, X3, Y3)