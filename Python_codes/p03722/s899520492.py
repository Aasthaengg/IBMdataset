n,m=map(int,input().split())
es=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    es.append((a-1,b-1,-c))

def bellman_ford(s,v,e,es):
    #s:始点　v:頂点数　e:辺の数　es:[s,t,c]
    d = [float("inf")]*v
    d[s] = 0

    for i in range(n):
        for p,q,r in es:
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                if i==n-1 and q==n-1:
                    print("inf")
                    exit()
    return d

d=bellman_ford(0,n,m,es)
print(-d[n-1])
