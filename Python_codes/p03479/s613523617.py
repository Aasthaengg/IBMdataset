x,y= list(map(int, input().split()))
ans=1
now=x
while True:
    if 2*now<=y:
        now*=2
        ans+=1
    else:
        print(ans)
        exit(0)