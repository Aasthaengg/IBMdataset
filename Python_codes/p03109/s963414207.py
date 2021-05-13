y,m,d = map(int, input().split("/"))

if y < 2019:
    print ("Heisei")
    exit ()

if y == 2019:
    if m < 4:
        print ("Heisei")
        exit ()
    elif m == 4:
        if d <= 30:
            print ("Heisei")
            exit ()
    else:
        pass

print ("TBD")
