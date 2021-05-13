while True:
    x,y=map(int,input().split())
    if(x==0):
        if(y==0):
            break
    if(y>x):
        print(f"{x} {y}")
    else:
        print(f"{y} {x}")

