X, Y = map(int, input().split())

if 0 <= X < Y or X < Y <= 0:
    print(Y-X)
elif 0 < Y < X or Y < X < 0:
    print(2+X-Y)
elif X < 0 < Y or Y < 0 < X:
    print(1+abs(X+Y))

if X == 0 and Y < 0:
    print(abs(Y)+1)
elif Y == 0 and X > 0:
    print(abs(X)+1)
