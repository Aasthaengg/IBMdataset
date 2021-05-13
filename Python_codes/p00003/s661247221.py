for i in range(input()):
    x=raw_input()
    L=map(int,x.split(" "))
    L.sort()
    if L[0]**2 + L[1]**2 == L[2]**2:
        print "YES"
    else:
        print "NO"