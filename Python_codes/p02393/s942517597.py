a, b, c = map(int, raw_input().split())
if    a <= b <= c:
    print"%d %d %d" % (a, b, c)
elif b <= a <= c:
    print"%d %d %d" % (b, a, c)
elif a <= c <= b:
    print"%d %d %d" % (a, c, b)
elif c <= a <= b:
    print"%d %d %d" % (c, a, b)
elif b <= c <= a:
    print"%d %d %d" % (b, c, a)
elif c <= b <= a:
    print"%d %d %d" % (c, b, a)