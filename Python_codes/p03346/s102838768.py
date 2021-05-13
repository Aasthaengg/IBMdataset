n=int(input())
l=[]
ll=[0]*(n+1)
s=set()
for i in range(n):
    p=int(input())
    l.append(p)
    ll[p]=i
tmp=0
ans=0
b=-1
for i in range(1,n+1):
    if b<ll[i]:
        tmp+=1
    else:
        tmp=1
    b=ll[i]
    ans=max(ans,tmp)
print(n-ans)



