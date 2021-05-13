a,b,c,d = map(int, input().split())

# print(a,b,c,d)

rectangle_x = a * b
rectangle_y = c * d

if rectangle_x > rectangle_y:
    print(rectangle_x)
elif rectangle_x < rectangle_y:
    print(rectangle_y)
else:
    print(rectangle_x)