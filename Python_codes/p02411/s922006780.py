while True:
    m,f,r=map(int, input().split())
    mf=m+f
    if m==f==r==-1:break
    elif min(m,f)==-1:
        print("F")
    elif mf>=80:
        print("A")
    elif mf>=65:
        print("B")
    elif mf>=50:
        print("C")
    elif mf>=30:
        if r>=50:
            print("C")
        else:
            print("D")
    else:
        print("F")
