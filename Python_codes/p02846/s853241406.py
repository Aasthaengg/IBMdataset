t1, t2 = (int(i) for i in input().split())
a1, a2 = (int(i) for i in input().split())
b1, b2 = (int(i) for i in input().split())

sa = t1*a1+t2*a2-t1*b1-t2*b2

if sa==0:
    print("infinity")
else:
    if sa>0:
        if a1>b1:
            print(0)
        else:
            ganba=t1*b1-t1*a1
            if ganba%sa!=0:
                gyakuten=(ganba//sa)+1
                print(gyakuten*2-1)
            else:
                gyakuten=(ganba//sa)+1
                print(gyakuten*2-2)
            #print(sa, ganba)
    else:
        sa=sa*(-1)
        if b1>a1:
            print(0)
        else:
            ganba=t1*a1-t1*b1
            if ganba%sa!=0:
                gyakuten=(ganba//sa)+1
                print(gyakuten*2-1)
            else:
                gyakuten=(ganba//sa)+1
                print(gyakuten*2-2)