while True:
    a, b = map(int, raw_input().split())
    if a==0 and b==0:
        break
    elif a > b:
        a, b = b, a
        print "%d %d" %(a,b)
    else:
        print "%d %d" %(a,b)