a, b, c, d = map(int,raw_input().split())
if abs(c-a) <= d or abs(a-b) <= d and abs(b-c) <= d:
    print "Yes"
else:
    print "No"
