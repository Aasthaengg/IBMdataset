s = input()
x = int(s)

y = 2
max_num = 1

for i in range(2, x):
    if i > x:
        break
    z = i
    y = z * z
    for j in range(2, x):
        if y <= x:
            max_num = max(max_num, y)
        else:
            break
        y *= z

print(max_num)