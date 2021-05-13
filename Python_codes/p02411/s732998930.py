while True:
    m,f,r = map(int,raw_input().split())
    if m==-1 and f==-1 and r==-1:
        break 
    mfsum = m+f
    if m==-1 or f==-1:
        print "F"
    elif mfsum >=80:
        print "A"
    elif mfsum >= 65 and mfsum <80:
        print "B"
    elif mfsum >= 50 and mfsum < 65:
        print "C"
    elif mfsum >=30 and mfsum < 50:
        if r >= 50:
            print "C"
        else: 
            print "D"
    else:
        print "F"