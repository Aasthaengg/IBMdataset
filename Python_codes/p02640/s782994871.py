X, Y = map(int, input().split())

if Y % 2 == 1:
    print("No")
elif Y < 2*X or 4*X < Y:
    print("No")
else:
    print("Yes")