n=int(input())
a=list(map(int,input().split()))

a.sort()
amx=max(a)+1
l=[True]*amx
ans=0

for i in range(n-1):
    if l[a[i]]:
        for j in range(a[i],amx,a[i]):
            l[j]=False
        if a[i]<a[i+1]:
            ans+=1

if l[-1]:
    ans+=1

print(ans)