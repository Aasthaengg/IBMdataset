n=int(input())
a=list(map(int,input().split()))
d=dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
ans=0
for key in d:
    if key<=d[key]:
        ans+=d[key]-key
    else:
        ans+=d[key]
print(ans)