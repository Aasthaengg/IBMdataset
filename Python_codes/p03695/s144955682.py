n = input()
rates = list(map(int, input().split()))
colors = [0, 0, 0, 0, 0, 0, 0, 0]
n_overrate = 0
n_colors = 0

for rate in rates:
    if 1 <= rate <= 399:
        colors[0] = 1
    elif 400 <= rate <= 799:
        colors[1] = 1
    elif 800 <= rate <= 1199:
        colors[2] = 1
    elif 1200 <= rate <= 1599:
        colors[3] = 1
    elif 1600 <= rate <= 1999:
        colors[4] = 1
    elif 2000 <= rate <= 2399:
        colors[5] = 1
    elif 2400 <= rate <= 2799:
        colors[6] = 1
    elif 2800 <= rate <= 3199:
        colors[7] = 1
    else:
        n_overrate += 1

sum_color = sum(colors)
if sum_color == 0:
    n_min_colors = 1
    n_max_colors = n_overrate
else:
    n_min_colors = sum_color
    n_max_colors = n_min_colors + n_overrate
print('{} {}'.format(n_min_colors, n_max_colors))
