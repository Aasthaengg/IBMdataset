n,m=map(int,input().split())
mist=[0 for i in range(m)]
for j in range(n):
    temp=list(map(int,input().split()))
    for s in range(1,len(temp)):
        mist[temp[s]-1]+=1

ans=sum(1 for x in mist if x==n)

print(ans)