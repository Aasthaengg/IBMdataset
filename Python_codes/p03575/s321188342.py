f=lambda:map(int,input().split())
n,m=f()
d=[[]for _ in range(n+1)]
c=[]
for _ in range(m):
    a,b=f()
    d[a]+=[b]
    d[b]+=[a]
    c+=[[a,b]]
ans=0
for i,j in c:
    a=[0]*(n+1)
    b=list(d[i])
    b.remove(j)
    now=0
    while b:
        now=b.pop(0)
        if a[now]==0:
            a[now]+=1
            for k in d[now]:
                if a[k]==0 and k!=i:
                    b+=[k]
    if a[j]==0:
        ans+=1
print(ans)