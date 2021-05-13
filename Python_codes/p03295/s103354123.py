N,M=map(int,input().split())
A=[]
B=[]
G=[[]for _ in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)

ans=0
cnt=0
while(1):
    if len(G[cnt])==0:
        cnt+=1
        continue
    m=min(G[cnt])
    break

while(1):
    cnt+=1
    if cnt>=N:
        break
    if cnt==m:
        #print(cnt,m)
        ans+=1
        while(1):
            if cnt==N:
                break
            if len(G[cnt])==0:
                cnt+=1
                continue
            m=min(G[cnt])
            break
    else:
        if len(G[cnt])==0:
            continue
        val=min(G[cnt])
        if val<m:
            m=val

print(ans)