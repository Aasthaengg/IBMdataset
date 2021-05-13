# ABC073 D - joisino's travel
import itertools
N,M,R=map(int, input().split())
r=list(map(int, input().split()))
inf=float("inf")
mat=[[inf]*N for _ in range(N)]

for i in range(M):
    a,b,c=map(int,input().split())
    if mat[a-1][b-1]>c:
        mat[a-1][b-1]=mat[b-1][a-1]=c

for i in range(R):
    r[i]-=1

ans=inf
for k in range(N):
    for i in range(N):
        for j in range(N):
            mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j])

for rr in itertools.permutations(r,R):
    t_sum=0
    for j in range(1,R):
        t_sum+=mat[rr[j-1]][rr[j]]
    ans=min(ans,t_sum)
print(int(ans))
