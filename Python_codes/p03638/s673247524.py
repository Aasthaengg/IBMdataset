h, w = map(int, input().split())
n = int(input())
amount = list(map(int, input().split()))
result = [[0 for i in range(w)] for j in range(h)]
down = True
total = 0
curr_col = 0
curr_index = 0
curr_color = 1
while total < w*h:
    if down:
        while curr_index < h and amount[curr_color - 1] > 0:
            result[curr_index][curr_col] = curr_color
            curr_index += 1
            amount[curr_color - 1] -= 1
            total += 1
        if curr_index == h:
            down = False
            curr_col += 1
            curr_index -= 1
        if amount[curr_color - 1] == 0:
            curr_color += 1
    else:
        while curr_index >= 0 and amount[curr_color - 1] > 0:
            result[curr_index][curr_col] = curr_color
            curr_index -= 1
            amount[curr_color - 1] -= 1
            total += 1
        if curr_index == -1:
            down = True
            curr_col += 1
            curr_index = 0
        if amount[curr_color - 1] == 0:
            curr_color += 1
for row in result:
    print(*row)