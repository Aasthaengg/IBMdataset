n=int(input())
a=list(map(int,input().split()))
a.append(0)
ans=0
t=a[0]
c=1
for i in range(1,n+1):
    if t==a[i]:
        c+=1
    else:
        ans+=c//2
        t=a[i]
        c=1
print(ans)