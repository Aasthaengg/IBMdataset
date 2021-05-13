k=int(input())
a=list(map(int,input().split()))
s=2+k*max(a)
l,r=s+1,0
while l-r>1:
    t=(l+r)//2
    p=t
    for i in a:
        t-=t%i
    if t>=2:
        l=p
    else:
        r=p
e=l
l,r=s+1,0
while l-r>1:
    t=(l+r)//2
    p=t
    for i in a:
        t-=t%i
    if t>2:
        l=p
    else:
        r=p
print(str(max(e,2))+" "+str(r)if r>e or r<2 else -1)