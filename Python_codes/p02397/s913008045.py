while True:
    x, y = map(int, raw_input().split())
    if x == 0 and y == 0:
        break
    else:
        if x > y:
            print str(y) + " " + str(x)
        else:
            print str(x) + " " + str(y)