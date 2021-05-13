x_1, y_1, x_2, y_2 = map(int, input().split())

l = x_2 - x_1
m = y_2 - y_1

print(x_2-m, y_2+l, x_1-m, y_1+l)