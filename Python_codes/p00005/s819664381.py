while True:
    try:
        a,b = map(int, raw_input().split())
        x,y = (a,b) if a > b else (b,a)
        
        while x%y:
            m = x % y
            x,y = y,m

        print "%d %d" % (y, a*b/y)
    except (EOFError):
        break