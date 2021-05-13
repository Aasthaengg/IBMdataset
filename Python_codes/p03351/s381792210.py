a, b, c, d = map(int, input().split())
d_ac = abs(c - a)
d_ab = abs(b - a)
d_bc = abs(c - b)
if d_ac <= d:
    print("Yes")
else:
    if d_ab <= d and d_bc <= d:
        print("Yes")
    else:
        print("No")

