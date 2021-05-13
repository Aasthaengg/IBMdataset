n=int(input())
a=list(map(int,input().split()))
a.sort()
minus=[i for i in a if i<0]
plus=[i for i in a if i>=0]
if len(minus)==0:
    print(a[-1]-a[0]+sum(a[1:n-1]))
    for i in range(n-1):
        if i==n-2:
            print(a[-1],a[n-2])
        else:
            print(a[i],a[i+1])
            a[i+1]=a[i]-a[i+1]
elif len(plus)==0:
    print(a[-1]-a[0]-sum(a[1:n-1]))
    print(a[-1],a[0])
    a[-1]=a[-1]-a[0]
    for i in range(1,n-1):
        print(a[-1],a[i])
        a[-1]-=a[i]
else:
    print(a[-1]-a[0]-sum(minus[1:])+sum(plus[0:-1]))
    for i in range(len(plus)-1):
        print(minus[0],plus[i])
        minus[0]-=plus[i]
    for i in range(len(minus)):
        print(a[-1],minus[i])
        a[-1]-=minus[i]