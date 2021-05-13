a,b,c,k=map(int,input().split())
if a>=k:
    print(k)
else:
    if a+b>=k:
        print(a)
    else:
        print(a+((k-a-b)*-1))