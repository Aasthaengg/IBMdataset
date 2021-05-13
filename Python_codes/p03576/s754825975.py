N,K=map(int,input().split())
x,y=[],[]
p=[]
for i in range(N):
    a,b=map(int,input().split())
    x.append(a);y.append(b)
    p.append((a,b))
x.sort()
y.sort()
ans=10**30
for r in range(N):
    for l in range(r):
        for u in range(N):
            for d in range(u):
                R,L,U,D=x[r],x[l],y[u],y[d]
                cnt=0
                m=(R-L)*(U-D)
                for i in range(N):
                    if p[i][0]>=L and p[i][0]<=R and p[i][1]>=D and p[i][1]<=U:
                        cnt+=1
                if cnt>=K:
                    ans=min(ans,m)
print(ans)