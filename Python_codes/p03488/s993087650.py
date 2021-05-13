S = input()
x, y = map(int, input().split())

x_axis = 1 << 8000
y_axis = 1 << 8000
first = True
axis = 0  # 0 = x, 1 = y
count = 0

for s in S:
    if s == 'T':
        if axis == 0:
            if first:
                x_axis = x_axis << count
            else:
                x_axis = (x_axis << count) | (x_axis >> count)
        else:
            y_axis = (y_axis << count) | (y_axis >> count)

        axis = 1 - axis  # 軸が変わる
        first = False
        count = 0

    else:
        count += 1

if count:
    if axis == 0:
        if first:
            x_axis = x_axis << count
        else:
            x_axis = (x_axis << count) | (x_axis >> count)
    else:
        y_axis = (y_axis << count) | (y_axis >> count)


if (x_axis >> (8000+x)) & 1 and (y_axis >> (8000+y)) & 1:
    print('Yes')
else:
    print('No')
