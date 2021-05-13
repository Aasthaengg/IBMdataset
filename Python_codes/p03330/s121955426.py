N,C=map(int,input().split())
D=[list(map(int,input().split()))for _ in range(C)]
c=[list(map(int,input().split()))for _ in range(N)]
cd=[[] for _ in range(3)]
for i in range(N):
    for j in range(N):
        cd[(i+j)%3].append(c[i][j]-1)
cost=[[0]*C for _ in range(3)]
for i in range(3):
    for j in range(C):
        for x in cd[i]:
            cost[i][j]+=D[x][j]
#print(cost)
from itertools import product
import pprint
A=list(product(range(C),repeat=3))
#print(A)
ans=float("inf")
for a in A:
    if a[0]==a[1] or a[1]==a[2] or a[2]==a[0]:
        continue
    cnt=0
    for i in range(3):
        cnt+=cost[i][a[i]]
    ans=min(ans,cnt)
print(ans)
