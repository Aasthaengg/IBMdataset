N,M=map(int,input().split())
XY=[list(map(int,input().split())) for i in range(M)]
def tsort(N,E):
    c=[[] for i in range(N)]
    t=[0]*N
    for i,j in E:
        c[i].append(j)
        t[j]+=1
    A,B=zip(*E)
    s=set(range(N))-set(B)
    l=[]
    while s:
        n=s.pop()
        l.append(n)
        for i in c[n]:
            t[i]-=1
            if t[i]==0:
                s.add(i)
    return c,l
c,l=tsort(N,[(x-1,y-1) for x,y in XY])
d=[0]*N
for i in l:
    for n in c[i]:
        d[n]=max(d[n],d[i]+1)
print(max(d))