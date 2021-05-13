a, b, c = map(int, raw_input() .split())
if a + b == c or a == b +c or a + c == b:
    print "Yes"
else:
    print "No"
