a,b,c=map(int,input().split())
if a%2!=0 or b%2!=0 or c%2!=0:
    print(0)
elif a==b==c:
    print(-1)
else:
    total=0
    while True:
        x=a/2
        y=b/2
        z=c/2
        a=y+z
        b=x+z
        c=x+y
        total+=1
        if a%2!=0 or b%2!=0 or c%2!=0:
            print(total)
            break