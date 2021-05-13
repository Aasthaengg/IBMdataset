from itertools import permutations

N,C=list(map(int,input().split()))
D=[list(map(int,input().split())) for _ in range(C)]
c=[list(map(int,input().split())) for _ in range(N)]

cnt=[[0]*(C+1) for _ in range(3)]
disc=[[0]*(C+1) for _ in range(3)]

for i in range(N):
    for j in range(N):
        cnt[(i+j)%3][c[i][j]]+=1

for i in range(3):
    for j in range(C):
        for k in range(C):
            disc[i][j]+=D[k][j]*cnt[i][k+1]
ans=10**10

for i,j,k in permutations(range(C),3):
    ans=min(ans,disc[0][i]+disc[1][j]+disc[2][k])

print(ans)