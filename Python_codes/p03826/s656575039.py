a, b, c, d = map(int,input().split())

X = a * b
Y = c * d

if X == Y:
    print(X)
elif X > Y:
    print(X)
else:
    print(Y)