import sys

for i in sys.stdin:
    i = i.split(" ")
    x, y = int(i[0]), int(i[1])
    if x == y == 0:
        break
    elif x <= y:
        print("{0} {1}".format(x, y))
    else:
        print("{0} {1}".format(y, x))