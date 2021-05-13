a,b =raw_input().split()
a,b = map(int,(a,b))
if a>b:
    a,b = map(str,(a,b))
    print "a > b"
elif a==b:
    a,b = map(str,(a,b))
    print "a == b"
else:
    a,b = map(str,(a,b))
    print "a < b"