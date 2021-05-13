K,T=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
ma=a[0]
su=sum(a)
res=su-ma
if T==1:
    print(su-1)
else:
    print(max(ma-res-1,0))
