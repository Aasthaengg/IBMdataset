while True:
    try:
        a, b = map(int, input().split())
        x, y = a, b
        while y:
            x, y = y, x%y
        print(x,int(a*b/x))
    except:
        break