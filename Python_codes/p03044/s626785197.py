N=int(input())
G=[[] for _ in [0]*(N+1)]
for _ in [0]*(N-1):
    u,v,w=map(int,input().split())
    G[u].append((v,w))
    G[v].append((u,w))

c=[0]*(N+1)
stack=[1]
c[1]=1
while stack:
    r=stack.pop()
    for nr,nw in G[r]:
        if c[nr]==0:
            stack.append(nr)
            if nw%2:
                c[nr]=-c[r]
            else:
                c[nr]=c[r]
for i in c[1:]:
    print((i+1)//2)