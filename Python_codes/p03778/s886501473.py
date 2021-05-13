W,a,b =map(int,input().split())
if b>a and b-(a+W)>0:
    print(b-(a+W))
elif b<a and a-(b+W)>0:
    print(a-(b+W))
else:
    print(0)
