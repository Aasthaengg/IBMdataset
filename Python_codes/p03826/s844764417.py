A,B,C,D=(int(x) for x in input().split())

X = A * B
Y = C * D

if X == Y or X > Y:
    print(X)

elif X < Y:
    print(Y)