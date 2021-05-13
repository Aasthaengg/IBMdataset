x,y=map(int,input().split())
if x%y==0:print(-1)
else:
    i=2
    while 1:
        if x*i%y!=0:
            print(x*i)
            break
        i+=1
        if i>10**18:
            print(-1)
            break