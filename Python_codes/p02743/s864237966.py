a,b,c = [int(x) for x in input().split()]

if c - b - a < 0:
    print("No")
else:
    if 4 * a * b < (c-b-a)**2:
        print("Yes")
    else:
        print("No")