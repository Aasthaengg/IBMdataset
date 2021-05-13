n,k=map(int,input().split())
v=list(map(int,input().split()))
times=min(n,k)
ans=0
for i in range(times+1):
    l=v[:i]
    for j in range(times-i+1):
        r=l+v[n-j:]
        rest=k-i-j
        val=sum(r)
        r=sorted(r)
        if len(r)>0:
            for p in range(min(rest,len(r))):
                if r[p]<0:
                    val-=r[p]
                else:
                    break
        if val>ans:
            ans=val
print(ans)