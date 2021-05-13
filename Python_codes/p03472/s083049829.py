n,h=map(int,input().split())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())
a_max=max(a)
b.sort()
ans=0
for bi in b[::-1]:
    if bi>a_max and h>0:
        h-=bi
        ans+=1
    else:
        break
if h>0:
    ans+=-(-h//a_max)
print(ans)