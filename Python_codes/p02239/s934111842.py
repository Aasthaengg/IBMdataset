from collections import deque

icase=0
if icase==0:
    n=int(input())
    u=[0]*n
#    g = [deque([]) for _ in range(n)]
    g = [[] for _ in range(n)]
    for i in range(n):
        ukv=list(map(int,input().split()))
        u[i]=ukv[0]-1
        ki=ukv[1]
        v=ukv[2:]
        for vi in v:
            g[u[i]].append(vi-1)
#            g[vi-1].append(u[i])
elif icase==1:
    n=4
    g = [[] for _ in range(n)]
    g[0]=[1,3]
    g[1]=[0,3]
    g[2]=[3]
    g[3]=[0,1,2]
#ans:0 1 2 1

q=deque([0])

stack=[0]
parent=[-1]*n
parent[0]=0
dist=[-1]*n
dist[0]=0
while q:
    state = q.popleft()
#    print("--- q:",q,"state:",state,"g:",g[state],"p:",parent)
    for v in g[state]:
#        print("  state:",state,"v:",v,"q:",q)
#        if parent[state] == v:
        if parent[v] !=-1:
            continue
        else:
#            print("parent:",parent,"xx:",xx,"stack",stack)
            parent[v]=state
            dist[v]=dist[state]+1
            q.append(v)
#            print(" state:",state,"v:",v,"parent:",parent,"stack",stack,"dist[v]",dist[v])

for i in range(n):
    print(i+1,dist[i])
    
