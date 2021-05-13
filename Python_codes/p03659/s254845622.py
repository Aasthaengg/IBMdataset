n=int(input())
a=list(map(int,input().split()))
aa=sum(a)-a[0]
tmp=a[0]
t=abs(tmp-aa)
ans=float("inf")
if ans>t:
    ans=t
for i in range(1,n-1):
    tmp+=a[i]
    aa-=a[i]
    t=abs(tmp-aa)
    if ans>t:
        ans=t
print(ans)