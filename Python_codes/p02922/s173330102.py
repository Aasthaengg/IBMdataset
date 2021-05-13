a,b=map(int,input().split())
if b==1:
    print("0")
elif b>1 and b<=a:
    print("1")
elif b>a:
    if (b-a)/(a-1)==(b-a)//(a-1):
        print((b-a)//(a-1)+1)
    else:
        print((b-a)//(a-1)+2)