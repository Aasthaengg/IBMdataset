N,A,B,C=list(map(int,input().split()))
l=[int(input()) for _ in range(N)]
target=sorted([0,A,B,C])
ans=10**10

for i in range(4**N):
    current=[0]*4
    cnt=[0]*4
    cost=0
    for j in range(N):
        b=i%4
        i//=4
        cnt[b]+=1
        current[b]+=l[j]

        if b>0 and cnt[b]>1:
            cost+=10
    
    current[0]=0
    current.sort()
    if current[1]==0:
        continue

    for j in range(1,4):
        cost+=abs(target[j]-current[j])

    ans=min(ans,cost)

print(ans)