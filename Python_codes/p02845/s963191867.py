n=int(input())
a=list(map(int,input().split()))
r,g,b=[-1],[-1],[-1]
ans=1
for i in range(n):
    f=1
    count=0
    if r[-1]==a[i]-1:
        count+=1
        r.append(a[i])
        f=0
    if g[-1]==a[i]-1:
        count+=1
        if f:
            g.append(a[i])
            f=0
    if b[-1]==a[i]-1:
        count+=1
        if f:
            b.append(a[i])
            f=0
    if f:
        print(0)
        exit()
    ans=(ans*count)%(10**9+7)
print(ans)