n=int(input())
a=[0]*n
l=[]
for i in range(n):
    a[i]=int(input())
    m=[]
    for j in range(a[i]):
        x=list(map(int,input().split()))
        m.append(x)
    l.append(m)


mx=0
for mask in range(1<<n):
    honest=[0]*n
    clear=True
    for i in range(n):
        if ((mask>>i)&1)==0:
            honest[i]+=1
    for i in range(n):
        if honest[i]==1:
            for k in range(a[i]):
                if honest[l[i][k][0]-1]!=l[i][k][1]:
                    clear=False
    if clear:
        ans=sum(honest)
        mx=max(ans,mx)

print(mx)
