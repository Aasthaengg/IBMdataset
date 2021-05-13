a,b,c,k=map(int,open(0).read().split())

if k<=a+b:
    print(min(a,k))
else:
    cntc=k-a-b
    print(a-cntc)