while True:
    ( x, y) = [ int(i) for i in input().split()]
    if x == 0 and y == 0:
        break
    else:
        if x > y:
            tmp = x
            x = y
            y = tmp
        print( '{0} {1}'.format( x, y))