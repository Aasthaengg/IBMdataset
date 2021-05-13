a, b, c, d = map(int, input().split())

square_1 = a * b
square_2 = c * d

if square_1 >= square_2:
    print(square_1)
else:
    print(square_2)