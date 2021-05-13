a,b,c=map(int,input().split())
a,b,c=sorted([a,b,c])
if (a+b+c)%2==1:
    if c%2==1:
        print((c*3-sum([a,b,c]))//2)
        exit()
    else:
        print((c*3+3-sum([a,b,c]))//2)
        exit()

else:
    if c%2==1:
        print((c*3+3-sum([a,b,c]))//2);exit()
    else:
        print((c*3-sum([a,b,c]))//2)
        exit()