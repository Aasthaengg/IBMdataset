for i in range(input()):
    a,b,c=sorted(map(int,raw_input().split()))
    print "YES" if a*a+b*b==c*c else "NO"