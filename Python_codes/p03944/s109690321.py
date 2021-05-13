W, H, N = map(int, input().split())
point_lst = [list(map(int, input().split())) for _ in range(N)]
x_1 = 0
x_2 = W
y_1 = 0
y_2 = H

for point in point_lst:
    if point[2] == 1:
        if point[0] > x_1:
            x_1 = point[0]

    elif point[2] == 2:
        if point[0] < x_2:
            x_2 = point[0]
    elif point[2] == 3:
        if point[1] > y_1:
            y_1 = point[1]
    else:
        if point[1] < y_2:
            y_2 = point[1]

width = x_2 - x_1 if x_2 > x_1 else 0
height = y_2 - y_1 if y_2 > y_1 else 0
print(width*height)