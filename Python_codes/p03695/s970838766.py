s = input()
n = int(s)

t_count = 0
f_count = 0
over = 0

colors = []
for i in range(8):
    colors.append(False)

v = input().split()

for i in range(n):
    x = int(v[i])
    if 1 <= x <= 399:
        colors[0] = True
    elif 400 <= x <= 799:
        colors[1] = True
    elif 800 <= x <= 1199:
        colors[2] = True
    elif 1200 <= x <= 1599:
        colors[3] = True
    elif 1600 <= x <= 1999:
        colors[4] = True
    elif 2000 <= x <= 2399:
        colors[5] = True
    elif 2400 <= x <= 2799:
        colors[6] = True
    elif 2800 <= x <= 3199:
        colors[7] = True
    else:
        over += 1

for i in range(len(colors)):
    if colors[i]:
        t_count += 1

if t_count == 0:
    min_ans = 1
else:
    min_ans = t_count
max_ans = t_count + over

print(min_ans, end=' ')
print(max_ans)

