a,b,c=map(int,input().split())
ans=0
average=int((a+b+c)/3)
while True:
    if a%2==1 or b%2==1 or c%2==1:
        print(ans)
        exit()
    else:
        tb=int(b/2)
        tc=int(c/2)
        ta=int(a/2)
        a=tb+tc
        b=ta+tc
        c=ta+tb

        ans+=1
    if a==average and b==average and c==average:
        print(-1)
        exit()
