d = int(input())
x = "Christmas"
y = "Eve"
if d == 25:
    print(x)
elif d == 24:
    print("{} {}".format(x, y))
elif d == 23:
    print("{} {} {}".format(x, y, y))
else:
    print("{} {} {} {}".format(x, y, y, y))