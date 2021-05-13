while True:
    n=map(int, raw_input().split())
    if n[0]==n[1]==n[2] == -1:
        break
    elif (n[0]==-1 or n[1]==-1) or int(n[0])+int(n[1]) < 30:
        print 'F'
    elif int(n[0])+int(n[1])>=80:
        print 'A'
    elif int(n[0])+int(n[1])>=65:
        print 'B'
    elif int(n[0])+int(n[1])>=50:
        print 'C'
    elif int(n[0])+int(n[1])>=30:
        if n[2]<50:
            print 'D'
        else:
            print 'C'
    else:
        print 'F'