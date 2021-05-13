K,T=map(int,input().split())
a=list(map(int,input().split()))
b=sum(a)
a.sort(reverse=True)
if T==1:
    print(a[0]-1)
else:
    if a[0]-(b-a[0])>=2:
        print(a[0]-(sum(a)-a[0])-1)
    else:
        print(0)