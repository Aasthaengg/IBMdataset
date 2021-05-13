n,d=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(d)]
cost=[[0]*d for _ in range(3)]
c=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        cost[(i+j)%3][c[i][j]-1]+=1
import itertools
ans=10**18
s=0
for p in itertools.permutations(range(1,d+1),3):
    for i in range(3):
        for j in range(d):
            s+=D[j][p[i]-1]*cost[i][j]
    if s<ans:
        ans=s    
    s=0
print(ans)