n,m,z = map(int, input().split())
r = list(map(int, input().split()))
wf=[[10**10 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = list(map(int,input().split()))
    wf[a-1][b-1] = c
    wf[b-1][a-1] = c

for i in range(n):
    wf[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            wf[i][j] = min(wf[i][j],wf[i][k]+wf[k][j])

from itertools import *
ans=10**10
for vils in list(permutations(r)):
    cnt=0
    for i in range(z-1):
        cnt+=wf[vils[i]-1][vils[i+1]-1]
    if ans>cnt:
        ans=cnt
print(ans)