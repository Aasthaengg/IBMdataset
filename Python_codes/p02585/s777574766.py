n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in range(n):
    p[i]-=1
ans=-10**18

for si in range(n):
    score=[]
    x=si
    while(1):
        x=p[x]
        score.append(c[x])
        if(x==si):
            break
    l=len(score)
    accum=[score[0]]
    for i in range(1,l):
        accum.append(score[i]+accum[i-1])
    total=sum(score)
    z=k//l
    if(total>0):
        for i in range(l):
            if(((z-1)*l+i)>=0):
                tmp=accum[i]+total*(z-1)
                ans=max(ans,tmp)
            if((z*l+i)<k):
                tmp=accum[i]+total*z
                ans=max(ans,tmp)
    else:
        for i in range(l):
            if(i<k):
                tmp=accum[i]
                ans=max(ans,tmp)
print(ans)