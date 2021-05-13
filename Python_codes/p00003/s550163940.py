for i in range(input()):
    q,w,e=sorted(map(int,raw_input().split()))
    print "YES" if q**2+w**2==e**2 else "NO"