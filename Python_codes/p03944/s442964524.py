W, H, N = map(int, input().split())
X1 = 0
X2 = W
Y1 = 0
Y2 = H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        if X1 <= x:
            X1 = x
        else:
            pass
    elif a == 2:
        if x <= X2:
            X2 = x
        else:
            pass
    if a == 3:
        if Y1 <= y:
            Y1 = y
        else:
            pass
    if a == 4:
        if y <= Y2:
            Y2 = y
        else:
            pass
if X1 >= X2 or Y1 >= Y2:
    print(0)
else:
    print((X2 - X1) * (Y2 - Y1))