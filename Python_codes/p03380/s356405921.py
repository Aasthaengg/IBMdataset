n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
x=a[n-1]/2
ans=a[0]
for i in range(1,n-1):
    if abs(ans-x)>abs(a[i]-x):
        ans=a[i]
print("{} {}".format(a[n-1],ans))