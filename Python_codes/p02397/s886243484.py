while True:
    x,y = map(int,raw_input().split())
    if x > y:
        print '%s %s' % (y,x)
    elif y > x:
        print '%s %s' % (x,y)
    elif x == 0 and y == 0:
        break
    else:
        print '%s %s' % (x,y)