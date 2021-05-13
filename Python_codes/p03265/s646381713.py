x_1, y_1, x_2, y_2 = map(int, input().split())

vec_x = -(y_2 - y_1)
vec_y = x_2 - x_1

x_3, y_3 = x_2 + vec_x, y_2 + vec_y
x_4, y_4 = x_1 + vec_x, y_1 + vec_y

print(x_3, y_3, x_4, y_4)
