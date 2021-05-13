T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
a = A1*T1-B1*T1
b = A2*T2-B2*T2

if a<0:
    if b<0:
        print(0)
    elif b==0:
        print(0)
    elif b>0:
        if a<-b:
            print(0)
        elif a==-b:
            print('infinity')
        else:
            d = a+b
            
            if a%d==0:
                n = (-a)//d-1
                print(2*n+2)
            else:
                n = (-a)//d
                print(2*n+1)
elif a==0:
    if b<0:
        print(1)
    elif b==0:
        print('infinity')
    elif b>0:
        print(1)
elif a>0:
    if b<0:
        if a>-b:
            print(0)
        elif a==-b:
            print('infinity')
        else:
            d = -a-b
            
            if a%d==0:
                n = a//d-1
                print(2*n+2)
            else:
                n = a//d
                print(2*n+1)
    elif b==0:
        print(0)
    elif b>0:
        print(0)