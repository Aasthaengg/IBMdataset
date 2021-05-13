x, a, b = map(int, raw_input() .split())
c = abs(a-x)
d = abs(b-x)
if c < d and d > c:
    print "A"
else:
    print "B"
