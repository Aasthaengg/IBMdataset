
icase=0
if icase==0:
    n=int(input())
    g=[[] for i in range(n)]
    for i in range(n-1):
        ui,vi,wi=map(int,input().split())
        wi=wi%2
        g[ui-1].append((vi-1,wi))
        g[vi-1].append((ui-1,wi))
elif icase==1:
    vv,e,r=4,5,0
    g = [[] for _ in range(vv)]
    g[0]=[(1,1),(2,4)]
    g[1]=[(2,2),(3,5)]
    g[2]=[(3,1)]
    n=3
    g=[[(1, 0)], [(0, 0), (2, 1)], [(1, 1)]]
elif icase==2:
    n=5
    g=[[(2, 0)], [(4, 0), (2, 0)], [(1, 0), (0, 0), (3, 0)], [(2, 0)], [(1, 0)]]

from heapq import heappop,heappush

q=[]
heappush(q,(0,0)) 

inf=float("INF")
dist=[inf]*(n)
dist[0]=0
while len(q)>0:
    dd,state = heappop(q)
#    print("dd:",dd,"state:",state,"q:",q)
    for v,dv in g[state]:
#        print("v:",v,"dv:",dv,"g[state]:",g[state],"parent[v]:",parent[v])
        if dist[v]>dist[state]+dv:
            dist[v]=dist[state]+dv
            heappush(q,(dist[v],v))
#            print(" state:",state,"v:",v,"dist[v]",dist[v])

for i in range(n):
    print(dist[i]%2)

