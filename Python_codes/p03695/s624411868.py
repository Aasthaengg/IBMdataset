n = int(input())
a = [int(i) for i in input().split()]
color = [0] * 8
any = 0
for i in a:
    if 1 <= i <= 399:
        color[0] = 1
    elif 400 <= i <= 799:
        color[1] = 1
    elif 800 <= i <= 1199:
        color[2] = 1
    elif 1200 <= i <= 1599:
        color[3] = 1
    elif 1600 <= i <= 1999:
        color[4] = 1
    elif 2000 <= i <= 2399:
        color[5] = 1
    elif 2400 <= i <= 2799:
        color[6] = 1
    elif 2800 <= i <= 3199:
        color[7] = 1
    else:
        any += 1
m = max(sum(color), 1)
M = sum(color) + any
print(m, M)
