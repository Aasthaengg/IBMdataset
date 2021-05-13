v = [int(x) for x in input().split()]
unit = 500

if v[0] * unit >= v[1]:
    print("Yes")
else:
    print("No")
