import math

n=int(input())
f=list()
p=list()
ans=-10**10
for i in range(n):
    f.append(list(map(int,input().split())))
for i in range(n):
    p.append(list(map(int,input().split())))
for i in range(1,1<<10):
    shop=list()
    cnt=[0]*n
    tmp=0
    for j in range(10):
        if i>>j&1:
            shop.append(j)
    for s in range(n):
        for k in shop:
            if(f[s][k]==1):
                cnt[s]+=1
        tmp+=p[s][cnt[s]]
    ans=max(ans,tmp)
print(ans)