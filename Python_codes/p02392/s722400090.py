def aizu002():
    xs = map(int,raw_input().split())
    a = xs[0]
    b = xs[1]
    c = xs[2]
    if a < b < c:
        print "Yes"
    else :
        print "No"

aizu002()