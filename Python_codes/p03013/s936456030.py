n,m=map(int,input().split())
a=[int(input()) for _ in range(m)]
if n==1:
    print(1)
    exit()
for i in range(m-1):
    if a[i+1]-a[i]==1:
        print(0)
        exit()
ans=1
a.append(n+1)
for i in range(m+1):
    if i==0:
        l=[1,1]
        for j in range(1,a[i]-1):
            l.append(l[-1]+l[-2])
        ans*=l[-1]
        ans%=(10**9 +7)
        #print(l)
    else:
        l=[1,1]
        for j in range(a[i-1]+2,a[i]-1):
            l.append(l[-1]+l[-2])
        ans*=l[-1]
        ans%=(10**9 +7)
        #print(l)
print(ans)