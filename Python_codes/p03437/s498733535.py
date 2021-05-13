x,y=map(int,input().split())
if x%y==0:
    print(-1)
else:
    if x*(y+1)<=10**18:
        print(x*(y+1))
    else:
        print(-1)