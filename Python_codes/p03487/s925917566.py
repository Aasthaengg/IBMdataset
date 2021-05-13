n=int(input())
a=list(map(int,input().split()))
l=[0 for i in range(10**5+1)]
ans=0
for i in range(n):
    if a[i]>10**5:
        ans+=1
    else:
        l[a[i]]+=1
for i in range(10**5+1):
    if 0<l[i]<i:
        ans+=l[i]
    if i<l[i]:
        t=l[i]-i
        ans+=t
print(ans)        