S = int(input())

X1 = Y1 = 0
X2 = 10**9; Y2 = 1
if S % (10**9) == 0:
    X3 = 0
else:
    X3 = 10**9 - S%(10**9)

Y3 = (S + X3) // (10**9)

print(X1, Y1, X2, Y2, X3, Y3)