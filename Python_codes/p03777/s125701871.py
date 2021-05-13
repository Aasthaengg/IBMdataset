icase=0
if icase==0:
    a,b=input().split()
    if a=="H":
        print(b)
    elif a=="D":
        if b=="H":
            print("D")
        elif b=="D":
            print("H")