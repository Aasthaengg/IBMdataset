def greatest_common_division(x, y):
    if x < y:
        x, y = y, x

    if y == 0 or x == y:
        return x
    else:
        return greatest_common_division(y, x % y)

x, y = map(int, input().split())
print(greatest_common_division(x, y))

