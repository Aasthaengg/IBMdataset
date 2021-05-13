s = int(input())
x_1 = y_1 = 0
if s < 10**9:
    x_2 = y_3 = 0
    x_3 = s
    y_2 = 1
elif s == 10**18:
    x_2 = 10**9
    x_3 = 0
    y_2 = 0
    y_3 = 10**9
else:
    digitnum = len(str(s))
    y_2 = 10**(digitnum-9)
    x_3 = s//y_2 + 1
    x_2 = x_3*y_2 - s
    y_3 = 1

print(x_1, y_1, x_2, y_2, x_3, y_3)