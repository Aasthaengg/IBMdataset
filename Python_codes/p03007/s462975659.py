n,*a=map(int,open(0).read().split())
a.sort()
print(sum(abs(i)for i in a)-2*min(abs(a[-1]),abs(a[0]))*(a[0]*a[-1]>0))
if a[0]>0:
    print(a[0],a[-1])
    a[0]-=a[-1]
    for i in a[1:-2]:
        print(a[0],i)
        a[0]-=i
    print(a[-2],a[0])
elif a[-1]<0:
    for i in a[:-1]:
        print(a[-1],i)
        a[-1]-=i
else:
    for i in a[1:-1]:
        if i<0:
            print(a[-1],i)
            a[-1]-=i
        else:
            print(a[0],i)
            a[0]-=i
    print(a[-1],a[0])