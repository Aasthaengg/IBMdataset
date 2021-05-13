for i in xrange(input()):
    a=map(lambda x: x**2,map(int,raw_input().split()))
    a.sort()
    if a[0]+a[1]==a[2]:
        print "YES"
    else:
        print "NO"