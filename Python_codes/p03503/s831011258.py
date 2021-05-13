n=int(input())
open=[]
for i in range(n):
    a=list(map(int,input().split()))
    open.append(a)
point=[]
for i in range(n):
    p=list(map(int,input().split()))
    point.append(p)

ans=-float("inf")
for i in range(1,2**10):
    tmp=0
    joi_open=[0]*10
    for j in range(10):
        if (i>>j)&1:
            joi_open[j]=1
    for j in range(n):
        cnt=0
        for k in range(10):
            if open[j][k]==joi_open[k]==1:
                cnt+=1
        tmp+=point[j][cnt]
    ans=max(ans,tmp)
print(ans)