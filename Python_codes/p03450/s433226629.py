n,m=map(int,input().split())
a=[None]*n
g=[[] for _ in range(n)]
for _ in range(m):
    l,r,d=map(int,input().split())
    g[l-1].append((r-1,d))
    g[r-1].append((l-1,-d))
for i in range(n):
    if a[i]==None:
        a[i]=0
        q=[i]
    while q:
        j=q.pop()
        for x,e in g[j]:
            if a[x]==None:
                a[x]=a[j]+e
                q.append(x)
            elif a[x]!=a[j]+e:
                print("No")
                exit()
                
print("Yes")
