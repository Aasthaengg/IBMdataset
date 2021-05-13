height_a, length_a, height_b, length_b = map(int, input().split())

rectangle_a = height_a * length_a
rectangle_b = height_b * length_b

if rectangle_a == rectangle_b:
    print(rectangle_a)
elif rectangle_a > rectangle_b:
    print(rectangle_a)
elif rectangle_b > rectangle_a:
    print(rectangle_b)