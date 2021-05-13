n=int(input())
a=sorted(list(map(int,input().split())))
max=a[-1]
min=a[0]
if n==2:
    print(max-min)
    print(max,min)
    exit()
ans=0
if a[-1]<0:
    ans+=-sum(a)+max*2
elif a[0]>0:
    ans+=sum(a)-min*2
else:
    for x in a:
        ans+=abs(x)
print(ans)
X=max
Y=min
for i in range(1,n-1):
    if a[i]>=0:
        x=Y
        y=a[i]
        print(x,y)
        Y=x-y    
    else:
        x=X
        y=a[i]
        print(x,y)
        X=x-y
print(X,Y)
