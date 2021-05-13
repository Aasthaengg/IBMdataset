W, H, N = map(int, input().split())
x_min, x_max, y_min, y_max = 0, W, 0, H 
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1 and x > x_min:
        x_min = x
    elif a == 2 and x < x_max:
        x_max = x
    elif a == 3 and y > y_min:
        y_min = y
    elif a == 4 and y < y_max:
        y_max = y
if x_max > x_min and y_max > y_min:
    S = (x_max - x_min) * (y_max - y_min)
else:
    S = 0
print(S)