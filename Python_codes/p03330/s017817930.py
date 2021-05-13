N,C=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(C)]
c=[list(map(int,input().split())) for _ in range(N)]
x=[[0]*(C+1) for _ in range(3)]
for i in range(N):
    for j in range(N):
        x[(i+j+2)%3][c[i][j]]+=1

from itertools import permutations
ans=1<<32
for ch in permutations(range(1,C+1),3):
    ans1=0
    for i in range(3):
        for j in range(1,C+1):
            ans1+=x[i][j]*d[j-1][ch[i]-1]
    ans=min(ans,ans1)
print(ans)
