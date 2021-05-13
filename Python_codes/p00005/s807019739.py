while True:
    try:
        a,b=map(int,input().split())
        y=a*b
        if b>a:
            a,b=b,a
        
        while a%b:
            x=a
            a,b=b,x%b

        print(b,int(y/b))

    except:
        break