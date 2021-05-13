W,a,b = map(int,input().split())
if a < b:
    l = b-(a+W)
    print(l if l>0 else 0)
elif a > b:
    l = a-(b+W)
    print(l if l>0 else 0)
else:
    print(0)
