from collections import defaultdict

n,m=map(int,input().split(' '))
paths=defaultdict(list)
ins=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split(' '))
    paths[x].append(y)
    ins[y]+=1

no_in=[y for y in range(1,n+1) if ins[y]==0]
depth=[0]*(n+1)
while no_in:
    x=no_in.pop()
    for y in paths[x]:
        ins[y]-=1
        depth[y]=max(depth[y],depth[x]+1)
        if ins[y]==0:
            no_in.append(y)

print(max(depth))