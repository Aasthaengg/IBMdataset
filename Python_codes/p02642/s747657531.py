n=int(input())
a=list(map(int,input().split()))

a.sort()
c=[0]*(10**6+1)
ans=0
for i in range(n):
    x=a[i]
    if c[x]:
        continue
    else:
        if i<=n-2:
            if x!=a[i+1]:
                ans+=1
        else:
            ans+=1
        for j in range(x,10**6+1,x):
            c[j]=1
print(ans)