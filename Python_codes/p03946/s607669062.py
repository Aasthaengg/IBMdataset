n,t=map(int,input().split())
l=list(map(int,input().split()))
m=l[-1]
ma=[m]*n
for i in range(n):
    m=max(m,l[n-1-i])
    ma[n-1-i]=m
for i in range(n):
    l[i]=ma[i]-l[i]
k=max(l)
ans=0
for i in l:
    if i==k:
        ans+=1
print(ans)