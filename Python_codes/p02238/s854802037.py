# =============================================================================
#　Depth First Search
# =============================================================================
import sys
sys.setrecursionlimit(10**8)

N=int(input())
Graph=[list(map(int,input().split()))[2:] for _ in range(N)]
Graph.insert(0,[])
seen=[False for _ in range(N+1)]
first_order=[0]*(N+1)
last_order=[0]*(N+1)
time=1

def dfs(Graph,v):
    global seen
    global time
    seen[v]=True
    first_order[v]=time
    time+=1
    for nv in Graph[v]:
        if seen[nv]:
            continue
        dfs(Graph,nv)

    last_order[v]=time
    time+=1

for v in range(1,N+1):
    if not seen[v]:
        dfs(Graph,v)
for i in range(1,N+1):
    print(i,first_order[i],last_order[i])

