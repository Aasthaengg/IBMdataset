while 1:
    k=input().split()
    a=int(k[0])
    b=int(k[1])
    c=int(k[2])
    if a==-1 and (b==-1 and c==-1):
        break
    if a<0 or b<0:
        print("F")
    elif a+b<30:
        print("F")
    elif a+b<50:
        if c>=50:
            print("C")
        else:
            print("D")
    elif a+b<65:
        print("C")
    elif a+b<80:
        print("B")
    else:
        print("A")

