
w, h, n = map(int, input().split())
square_info = [list(map(int, input().split())) for _ in range(n)]

min_x = 0
max_x = w
min_y = 0
max_y = h

for i in range(n):
    if square_info[i][2] == 1:
        min_x = max(min_x, square_info[i][0])
    elif square_info[i][2] == 2:
        max_x = min(max_x, square_info[i][0])
    elif square_info[i][2] == 3:
        min_y = max(min_y, square_info[i][1])
    else:
        max_y = min(max_y, square_info[i][1])

if max_x <= min_x or max_y <= min_y:
    print(0)
else:
    print((max_x - min_x)*(max_y - min_y))