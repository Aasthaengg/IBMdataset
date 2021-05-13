while 1:
    m, f, r = map(int, raw_input().split())
    sum = m + f
    if sum == -2: break
    elif min(m, f) == -1: print 'F'
    elif sum >= 80: print 'A'
    elif sum >= 65: print 'B'
    elif sum >= 50: print 'C'
    elif sum >= 30:
        if r >= 50: print 'C'
        else: print 'D'
    else: print 'F'