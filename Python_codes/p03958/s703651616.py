k,t=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a, reverse=True)

if len(a)>1:
    x=a[0]-sum(a[1:])
    if x>0:
        print(x-1)
    else:
        print(0)
else:
    print(a[0]-1)