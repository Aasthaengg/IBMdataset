N,M=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(M)]
ab.sort(key=lambda x:x[1])
now=0
ans=0
for i in range(M):
    if now<=ab[i][0]:
        now=ab[i][1]
        ans+=1
print(ans)