W,a,b=list(map(int,input().split()))
if a<=b:
    d=b-(a+W)
    if d<=0:
        print(0)
        exit()
    print(d)
else:
    d=a-(b+W)
    if d<=0:
        print(0)
        exit()
    print(d)
