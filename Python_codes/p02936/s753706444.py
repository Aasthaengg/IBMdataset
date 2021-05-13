import sys
sys.setrecursionlimit(4*(10**6))

N,Q=map(int,input().split())
edge=[[] for _ in range(N+1)]
score=[0]*(N+1)
for _ in range(N-1):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

for _ in range(Q):
    p,x=map(int,input().split())
    score[p]+=x

visited=set()

def dfs(v):
    global score
    visited.add(v)
    for i in edge[v]:
        if i in visited:
            continue
        score[i]+=score[v]
        dfs(i)

dfs(1)
print(*score[1:])