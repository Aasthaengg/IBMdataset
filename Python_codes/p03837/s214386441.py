# ABC051 D - Candidates of No Shortest Paths
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
def WF():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])

n,m=nm()
aa=[]
bb=[]
cc=[]
d=[[0]*n for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    aa.append(a)
    bb.append(b)
    cc.append(c)
for i in range(n):
    for j in range(n):
        if i==j:
            d[i][j]=0
        else:
            d[i][j]=10**5

for i in range(m):
    d[aa[i]][bb[i]]=min(d[aa[i]][bb[i]],cc[i])
    d[bb[i]][aa[i]]=min(d[bb[i]][aa[i]],cc[i])
WF()

ans=m
for i in range(m):
    short=False
    for j in range(n):
        if d[j][aa[i]]+cc[i]==d[j][bb[i]]:
            short=True
    if short:
        ans-=1
print(ans)
