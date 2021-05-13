x, a, b = map(int, raw_input() .split())
if b > a and b - a <= x:
    print "safe"
elif b > a and b - a >= x + 1:
    print "dangerous"
elif b <= a:
    print "delicious"
