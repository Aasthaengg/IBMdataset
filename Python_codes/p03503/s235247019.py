n=int(input())
f=[]
for i in range(n):
    tmp=0
    op=list(map(int,input().split()))
    for j in range(10):
        tmp+=op[j]<<j
    f.append(tmp)

p=[]
for i in range(n):
    p.append(list(map(int,input().split())))

ans=-10**12
for i in range(1, 1<<10):
    tmp=0
    for j in range(n):
        consist=f[j]&i
        cnt=0
        for k in range(10):
            if (consist>>k)%2:
                cnt+=1
        tmp+=p[j][cnt]
    ans=max(ans,tmp)
print(ans)