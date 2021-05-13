import sys
sys.setrecursionlimit(10**8)

N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)


dist=[float("inf")]*N
dist[0]=0
prev=[None]*N

def dfs1(v,parent,d):
    prev[v]=parent
    dist[v]=d
    for v2 in graph[v]:
        if v2==parent:
            continue
        dfs1(v2,v,d+1)

dfs1(0,-1,0)

x=N-1
for _ in range((dist[-1]-1)//2):
    x=prev[x]
cant_go=prev[x]

sunuke_score=0
def dfs2(v,parent):
    global sunuke_score
    sunuke_score+=1
    for v2 in graph[v]:
        if v2==parent:
            continue
        if v2==cant_go:
            continue
        dfs2(v2,v)

dfs2(x,-1)

fennec_score=N-sunuke_score
if sunuke_score>=fennec_score:
    print("Snuke")
else:
    print("Fennec")