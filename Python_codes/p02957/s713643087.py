a,b=map(int,input().split())
c=abs(a-b)
if c%2==1:
    print("IMPOSSIBLE")
else:
    print((a+b)//2)
