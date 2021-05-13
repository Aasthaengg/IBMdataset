n = int(input())
A = list(map(int, input().split()))
color = []
other = 0
for a in A:
    if a < 400: color.append(1)
    elif a < 800: color.append(2)
    elif a < 1200: color.append(3)
    elif a < 1600: color.append(4)
    elif a < 2000: color.append(5)
    elif a < 2400: color.append(6)
    elif a < 2800: color.append(7)
    elif a < 3200: color.append(8)
    else: other += 1
c = len(set(color))
if color: print(c, c+other)
else: print(1, other)