n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
maxn=0
for i in range(8):
    vec=[]
    for j in range(n):
        s=0
        for k in range(3):
            if(int(i/(1<<k))%2==0):
                s+=a[j][k]
            else:
                s-=a[j][k]
        vec.append(s)
    ans=0
    vec.sort(reverse=True)
    for j in range(m):
        ans+=vec[j]
    maxn=max(maxn,ans)
print(maxn)