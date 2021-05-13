n,k=map(int,input().split())
a=[int(i) for i in input().split()]
res=100000000000000000000
for i in range(n-k+1):
    l=a[i]
    r=a[i+k-1]
    if l<=0<=r:
        res=min(res,(-l+r)*2-max(-l,r))
    elif r<0:
        res=min(res,-l)
    else:
        res=min(res,r)
print(res)
