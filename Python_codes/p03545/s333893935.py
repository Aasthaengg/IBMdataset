import sys

a, b, c, d = list(map(int, input().rstrip()))

li = ["+", "-"]

for x in li:
    for y in li:
        for z in li:
            tmp = a
            if x == "+":
                tmp += b
            else:
                tmp -= b
            if y == "+":
                tmp += c
            else:
                tmp -= c
            if z == "+":
                tmp += d
            else:
                tmp -= d
            if tmp == 7:
                print("{}{}{}{}{}{}{}=7".format(a, x, b, y, c, z, d))
                sys.exit()