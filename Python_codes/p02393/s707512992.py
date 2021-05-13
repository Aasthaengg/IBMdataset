a, b, c = map(int, input().split())

if a <= b:
    if b <= c:
        print("{0} {1} {2}".format(a, b, c))
    elif c <= a:
        print("{0} {1} {2}".format(c, a, b))
    else:
        print("{0} {1} {2}".format(a, c, b))

else:
    if a <= c:
        print("{0} {1} {2}".format(b, a, c))
    elif c <= b:
        print("{0} {1} {2}".format(c, b, a))
    else:
        print("{0} {1} {2}".format(b, c, a))