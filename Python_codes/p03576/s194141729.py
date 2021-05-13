n,k=map(int,input().split())
P,X,Y=[],[],[]
for _ in range(n):
    x,y=map(int,input().split())
    P.append((x,y))
    X.append(x)
    Y.append(y)
ans=10**19
X.sort()
Y.sort()
for d in range(n-1):
    for u in range(d,n):
        for l in range(n-1):
            for r in range(l,n):
                D,U,L,R=X[d],X[u],Y[l],Y[r]
                cnt=0
                for i in P:
                    if D<=i[0]<=U and L<=i[1]<=R:
                        cnt+=1
                if cnt>=k:
                    ans=min(ans,(U-D)*(R-L))
print(ans)
