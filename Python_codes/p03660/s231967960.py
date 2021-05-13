# coding: utf-8
N=int(input())
G=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

INF=10**9

d=[INF for i in range(N)]
edges=[0 for i in range(N)]
d[0]=0
queue=[]
queue.append(0)

while queue:
    u=queue.pop(0)
    for i in range(len(G[u])):
        if d[G[u][i]]==INF:
            queue.append(G[u][i])
            d[G[u][i]]=d[u]+1

k=d[N-1]
m=N-1
queue.append(N-1)

while k>d[N-1]//2+1:
    u=queue.pop(0)
    for i in range(len(G[u])):
        if d[G[u][i]]==d[u]-1:
            queue.append(G[u][i])
            k=d[u]
            m=u

queue=[]
queue.append(m)
unused=[True for i in range(N)]
unused[m]=False

sunuke=1

while queue:
    u=queue.pop(0)
    sunuke+=len(G[u])-1
    for i in range(len(G[u])):
        if d[G[u][i]]>d[u] and unused[G[u][i]]:
            queue.append(G[u][i])
            unused[G[u][i]]=False

if sunuke>=-(-N//2):
    print("Snuke")
else:
    print("Fennec")
    
    
    
    

