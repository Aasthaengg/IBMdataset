w,a,b=map(int,input().split())
if b>=a:
    print(b-(a+w) if b-(a+w)>0 else 0)
else:
    print(a-(b+w) if a-(b+w)>0 else 0)