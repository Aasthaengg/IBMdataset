import sys
sys.setrecursionlimit(100000)

N=int(input())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    A,B=map(int,input().split())
    edges[A-1].append(B-1)
    edges[B-1].append(A-1)
prevs=[0]*N
def dfs(prev,curr):
    prevs[curr]=prev
    if curr == N-1:
        return
    for c in edges[curr]:
        if c!=prev:
            dfs(curr,c)
dfs(-1,0)
paths=[N-1]
tmp=N-1
while tmp!=0:
    paths.append(prevs[tmp])
    tmp=prevs[tmp]
paths=paths[::-1]

points=[0,0]
def count(prev,curr,player):
    points[player]+=1
    for c in edges[curr]:
        if c!=prev:
            count(curr,c,player)

nf = (len(paths)+1)//2
f,s = paths[nf-1],paths[nf]
count(s,f,0)
count(f,s,1)
pf,ps=points
print("Fennec" if pf>ps else "Snuke")
