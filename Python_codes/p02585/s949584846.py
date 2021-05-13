INF=10**20

N,K=map(int,input().split())

array=list(map(int,input().split()))
P=[]
C=list(map(int,input().split()))
for i in array:
    P.append(i-1)

ans=-1*INF

for i in range(N):
    v=i
    cycle_sum=0
    cycle_cnt=0

    while(True):
        cycle_cnt+=1
        cycle_sum+=C[v]
        v=P[v]
        if v==i:
            break

    path=0
    cnt=0

    while(True):
        cnt+=1
        path+=C[v]

        if cnt>K:
            break

        num=(K-cnt)//cycle_cnt
        score=path+max(0,cycle_sum)*num
        ans=max(ans,score)

        v=P[v]
        if v==i:
            break

print(ans)