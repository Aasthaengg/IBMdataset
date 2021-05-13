A, B, C, D = map(int, input().split())

Rect1 = int(A*B)

Rect2 = int(C*D)

if (Rect1 > Rect2):
    print(Rect1)

elif (Rect1 < Rect2):
    print(Rect2)

else:
    print(Rect1)