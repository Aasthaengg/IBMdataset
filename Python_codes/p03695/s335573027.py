n = int(input())
l = list(map(int, input().split()))
d = set()
over = 0
for i in l:
    if i <= 399:
        d.add("gray")
    elif i <= 799:
        d.add("brown")
    elif i <= 1199:
        d.add("green")
    elif i <= 1599:
        d.add("light blue")
    elif i <= 1999:
        d.add("blue")
    elif i <= 2399:
        d.add("yellow")
    elif i <= 2799:
        d.add("orange")
    elif i <= 3199:
        d.add("red")
    else:
        over += 1

min_color = len(d)
if len(d) == 0:
    min_color +=1
max_color = len(d) + over

print(min_color, max_color)
