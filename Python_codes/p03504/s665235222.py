n,C=list(map(int,input().split()))
part=[[0]*(3*10**5) for _ in range(31)]
part2=[0]*(3*10**5)

for _ in range(n):
    s,t,c=list(map(int,input().split()))

    part[c][s]+=1
    part[c][t]-=1

for i in range(1,C+1):
    for j in range(1,10**5+1):
        if part[i][j]==1:
            part2[2*j-1]+=1
        elif part[i][j]==-1:
            part2[2*j]-=1

ans=0
for i in range(1,2*10**5+1):
    part2[i]+=part2[i-1]
    ans=max(ans,part2[i])

print(ans)