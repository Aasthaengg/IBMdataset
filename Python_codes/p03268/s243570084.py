n,k=map(int,input().split())

if k/2==k//2:
    p=n//(k//2)

    if p==0:
        print(0)
    elif p==1:
        print(1)
    elif p==2:
        print(2)
    elif p==3:
        print(9)
    elif p==4:
        print(16)
    else:
        m=16
        for i in range(5,p+1):
            m+=1+6*((-(-i//2))-1)+6*((-(-i//2))-1)*(-(-i//2)-2)//2
        print(m)
    
else:
    p=n//k

    if p==0:
        print(0)
    elif p==1:
        print(1)
    elif p==2:
        print(8)
    else:
        m=8
        for i in range(3,p+1):
            m+=1+6*(i-1)+6*(i-1)*(i-2)//2
        print(m)
