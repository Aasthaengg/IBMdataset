n,m=map(int,input().split())
ks=[]
for i in range(m):
    temp=list(map(int,input().split()))
    ks.append(temp)
p=list(map(int,input().split()))
cnt_ans=0
for i in range(1<<n):
    cnt_on=0
    for j in range(0,m):
        cnt=0
        for k in range(1,ks[j][0]+1):
            if (i>>(ks[j][k]-1))%2==1:
                cnt+=1
        if cnt%2==p[j]:
            cnt_on+=1
    if cnt_on==m:
        cnt_ans+=1
print(cnt_ans)

