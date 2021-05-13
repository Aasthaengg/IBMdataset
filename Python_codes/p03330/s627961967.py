from collections import defaultdict as dd
N,C=map(int,input().split())
d=[list(map(int,input().split())) for i in range(C)]
c=[list(map(int,input().split())) for i in range(N)]
table=[dd(int) for i in range(3)]

for i in range(N):
    for j in range(N):
        k=(i+j)%3
        table[k][c[i][j]-1]+=1

ans=10**10
for i in range(C):
    t1=0
    for x in table[0]:
        t1+=d[x][i]*table[0][x]
    for j in range(C):
        if i==j:continue
        t2=0
        for x in table[1]:
            t2+=d[x][j]*table[1][x]
        for k in range(C):
            if i==k or j==k:continue
            t3=0
            for x in table[2]:
                t3+=d[x][k]*table[2][x]
            
            ans=min(ans,t1+t2+t3)
print(ans)


