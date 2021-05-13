a,b,c=map(int,raw_input().split())
if a+b >= c:
    print "No"
else:
    q = 4 * a * b;
    h = (c - a - b) * (c - a - b)
    if q < h:
        print "Yes"
    else:
        print "No"