N=int(input())
a=list(map(int,input().split()))

chk=[0 for i in range(N)]
ans=0
for i in range(N):
    if chk[i]==1:
        continue
    if a[a[i]-1]==(i+1):
        ans+=1
        chk[i]=1
        chk[a[i]-1]=1
    else:
        chk[i]=1

print(ans)