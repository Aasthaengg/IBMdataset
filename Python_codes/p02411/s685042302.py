while True:
    v = map(int,raw_input().split())
    if v[0] == -1 and v[1] == -1 and v[2] == -1:
        break
    if v[0] * v[1] < 0:
        print 'F'
    else:
        s = v[0] + v[1]
        if s >= 80:
            print 'A'
        elif s >= 65:
            print 'B'
        elif s >= 50:
            print 'C'
        elif s >= 30:
            if v[2] >= 50:
                print 'C'
            else:
                print 'D'
        else:
            print 'F'