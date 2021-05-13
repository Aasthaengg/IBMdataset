n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
s=0
ans=0
for i in range(n):
    s+=a[i]
    if s<=x:
        ans+=1
    else:
        break
if s<x:
    ans=n-1
print(ans)