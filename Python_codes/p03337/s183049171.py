A, B = map(int, input().split())
X = A + B
Y = A - B
Z = A * B
if X >= Y and X >= Z:
    print(X)
elif Y >= X and Y >= Z:
    print(Y)
elif Z >= X and Z >= Y:
    print(Z)