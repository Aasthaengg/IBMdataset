a,b,x=map(int,input().split())
if a%x>0 and b%x>0:
    print(b//x-a//x)
elif b%x==0 and a%x>0:
    print(b//x-a//x)
else:
    print(b//x-a//x+1)

