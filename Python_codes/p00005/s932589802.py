while 1:
    try:
        x,y=[int(i) for i in input().split()]
        a=x
        b=y

        while 1:
            c=x%y
            if x%y==0:
                print(y,a*b//y)
                break
            else:
                x=y
                y=c
    except EOFError:
        break