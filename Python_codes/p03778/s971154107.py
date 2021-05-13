w,a,b=map(int,input().split())
c=min(a,b)
d=max(a,b)
if c+w<d:
    print(d-c-w)
else:
    print(0)