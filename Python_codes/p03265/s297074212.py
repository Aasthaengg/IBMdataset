def actual(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1

    x3, y3 = x2 - b, y2 + a
    x4, y4 = x3 - a, y3 - b

    # return f'{x3} {y3} {x4} {y4}'
    return '{} {} {} {}'.format(x3, y3, x4, y4)

x1, y1, x2, y2 = map(int, input().split())
print(actual(x1, y1, x2, y2))
