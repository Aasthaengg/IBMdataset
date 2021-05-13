while True:
    a=input().split()
    h=int(a[0])
    w=int(a[1])
    if h==0 and w==0:
        break
    count=0
    count2=0
    for i in range(h):
        count=1
        if count2%2==1:
            count=0
        count2+=1
        for i in range(w):
            if count%2==1:
                print("#",end="")
            else:
                print(".",end="")
            count+=1
        print()
    print()
        

