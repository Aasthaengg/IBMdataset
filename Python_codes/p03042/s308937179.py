s = input()

l = list(s)

x = int(l[0]+l[1])
y = int(l[2]+l[3])

if 0 < x < 13 and (y > 12 or y == 0):
    print("MMYY")
elif (x > 12 or x == 0) and 0 < y < 13:
    print("YYMM")
elif x > 12 or y > 12 or (x == 0 and y == 0):
    print("NA")
else:
    print("AMBIGUOUS")