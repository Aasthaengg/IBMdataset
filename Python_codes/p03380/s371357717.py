import bisect

n=int(input())
a=list(map(int,input().split()))
a.sort()
k=bisect.bisect_left(a,a[-1]/2)

if k==n-1:
    print(a[-1],a[-2])
elif k==0:
    print(a[-1],a[0])
else:
    if a[-1]/2-a[k-1]<a[k]-a[-1]/2:
        k-=1
    print(a[-1],a[k])
