def MI():
    return map(int,input().split())
n,m,q=MI()
t=[[0]*(1+n) for _ in range(1+n)]
for i in range(m):
    l,r=MI()
    t[l][r]+=1
for i in range(n):
    for j in range(n):
        t[i+1][j+1]+=t[i+1][j]+t[i][j+1]-t[i][j]

for i in range(q):
    p,q=MI()
    p-=1
    print(t[q][q]-t[q][p]-t[p][q]+t[p][p])
