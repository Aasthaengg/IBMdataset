
a, b, c = [int(x) for x in input().split()]
#a, b, c = [249999999, 250000000, 999999998]
d = c - a - b

if d <= 0:
    print("No")
else:
    if 4 * a * b < d * d:
        print("Yes")
    else:
        print("No")