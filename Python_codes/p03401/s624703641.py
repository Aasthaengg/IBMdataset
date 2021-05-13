n=int(input())
a=[0]+list(map(int,input().split()))
su=0
su+=abs(a[1])
for i in range(2,n+1):
    su+=abs(a[i]-a[i-1])
su+=abs(a[n])
a.append(0)
#print(su)
for i in range(1,n+1):
    x,y=a[i-1],a[i+1]
    if min(x,y)<=a[i] and a[i]<=max(x,y):
        print(su)
    else:
        d1=abs(a[i-1]-a[i])
        d2=abs(a[i]-a[i+1])
        print(su-2*min(d1,d2))

