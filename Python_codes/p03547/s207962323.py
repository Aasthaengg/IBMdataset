xy = input()
x, y = xy[0], xy[2]

if x < y:
    print("<")
elif x == y:
    print("=")
else:
    print(">")