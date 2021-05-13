n=int(input())
print(0)
s=input()
if s=="Vacant":
    exit()
print(n-1)
t=input()
if t=="Vacant":
    exit()
l,r=0,n
for i in range(18):
    mid=(l+r)//2
    print(mid)
    m=input()
    if m=="Vacant":
        exit()
    if (mid-l)%2:
        if s==m:
            r=mid
            t=m
        else:
            l=mid
            s=m
    else:
        if s==m:
            l=mid
            s=m
        else:
            r=mid
            t=m