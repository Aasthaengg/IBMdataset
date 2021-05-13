N,M,P=map(int,input().split())
ABC=[list(map(int,input().split())) for i in range(M)]
c=[[] for i in range(N)]
v=[0]*N
for a,b,_ in ABC:
    c[a-1].append(b-1)
q=[0]
while q:
    p=q.pop()
    if v[p]==0:
        v[p]=1
        for n in c[p]:
            if n!=p:
                q.append(n)
inf=10**20
f=lambda i,j,w: [i-1,j-1,P-w]
edge=[f(i,j,w) for i,j,w in ABC if v[i-1]]
def bf(N,s):
    d=[inf]*N
    d[s]=0
    prev=[-1]*N
    for i in range(N-1):
        f=0
        for i,j,w in edge:
            if d[j]>d[i]+w:
                d[j]=d[i]+w
                prev[j]=i
                f=1
        if f==0:
            break
    while True:
        f=0
        for i,j,w in edge:
            if d[j]>d[i]+w and (d[j]!=-inf or d[i]!=-inf):
                d[i]=d[j]=-inf
                f=1
        if f==0:
            break
    return d
d=bf(N,0)
print(max(0,-d[-1]) if d[-1]>-inf else -1)