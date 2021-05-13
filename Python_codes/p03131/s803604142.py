k,a,b =  map(int,input().split())

c = b-a

if c >1:
    if k < a-1:
        print(1+k)
        exit(0)
    else:
        d=(k-a+1)
        if d %2==0:
            print(c*(d//2)+a)
        else:
            print(c*(d//2)+a+1)
        exit(0)
else:
    print(1+k)