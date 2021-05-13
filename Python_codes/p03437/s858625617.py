x,y=map(int,input().split())
i=x
l=False
if x==y or x%y==0:
    print(-1)
else:
    while 1<=i and i<=x*y:
        if i%x==0 and i%y!=0:
            print(i)
            l=True
            break
        else:
            i+=x